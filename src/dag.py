from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import os
import sys

# Add DAGs folder to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from authenticate_gmail import authenticate_gmail
from extract import list_emails
from load import load_data_into_csv, add_sentiment_result

os.environ['GROQ_API_KEY'] = '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'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def authenticate_task(**kwargs):
    """Simply verify authentication works"""
    service = authenticate_gmail()
    profile = service.users().getProfile(userId='me').execute()
    print(f"Authenticated as: {profile['emailAddress']}")
    return True

def process_emails_task(**kwargs):
    """Process emails with fresh service instance"""
    service = authenticate_gmail()
    # Your email processing logic here
    # messages = service.users().messages().list(userId='me', maxResults=10).execute()
    # print(f"Processed {len(messages.get('messages', []))} messages")
    return True

def list_emails_task(**kwargs):
    """Task to list emails from Gmail"""
    service = authenticate_gmail()
    data = list_emails(service)
    print(f"first email: {data[0]}")
    # Push the extracted data to XCom

def load_data_task(**kwargs):
    """Task to load data into CSV"""
    service = authenticate_gmail()
    data = list_emails(service)
    load_data_into_csv(data)
    # Push the file path for the next task (assuming load_data_into_csv returns path)

def analyze_sentiment_task(**kwargs):
    service = authenticate_gmail()
    data = list_emails(service)
    load_data_into_csv(data)
    add_sentiment_result("/home/ubuntu/email_data.csv")

with DAG(
    'gmail_processing_pipeline',
    default_args=default_args,
    description='Process Gmail emails every 5 minutes',
    schedule_interval=timedelta(minutes=5),  # Changed to run every 5 minutes
    start_date=days_ago(1),
    catchup=False,
    max_active_runs=1,  # Prevents overlapping runs
    tags=['gmail', 'frequent'],
) as dag:

    verify_auth = PythonOperator(
        task_id='verify_authentication',
        python_callable=authenticate_task
    )

    process_emails = PythonOperator(
        task_id='process_emails',
        python_callable=process_emails_task
    )

    process_list_emails = PythonOperator(
        task_id='list_emails',
        python_callable=list_emails_task
    )

    process_load_data = PythonOperator(
        task_id='load_data',
        python_callable=load_data_task
    )

    process_analyze_sentiment = PythonOperator(
        task_id='analyze_sentiment',
        python_callable=analyze_sentiment_task
    )

    verify_auth >> process_emails >> process_list_emails >> process_load_data >> process_analyze_sentiment