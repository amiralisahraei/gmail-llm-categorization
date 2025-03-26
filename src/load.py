from datetime import date
import pandas as pd
from sentiment_analysis import model_response

def load_data_into_csv(data, output_path='email_data.csv'):
    """Convert the provided data into a DataFrame and save it as a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)

def add_sentiment_result(dataset_path):
    """Add sentiment analysis results to the dataset and save it as a CSV file."""
    df = pd.read_csv(dataset_path)
    df["Result"] = df["body"].apply(model_response)
    # create a new column for the date of creation
    today_date = date.today()
    date_array = df.shape[0]*[today_date]
    df["Date"] = date_array
    df.to_csv(dataset_path, index=False)