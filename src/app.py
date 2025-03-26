import time
import datetime
from authenticate_gmail import authenticate_gmail
from extract import list_emails
from load import load_data_into_csv, add_sentiment_result


def process_emails(data_path='email_data.csv'):
    """Authenticate Gmail, extract emails, load data into CSV, and add sentiment results."""
    service = authenticate_gmail()
    email_data = list_emails(service)
    load_data_into_csv(email_data)
    add_sentiment_result(data_path)


def log_current_time():
    """Log the current time in HH:MM:SS format."""
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    print(f"Waiting for 5 minutes before the next execution, current time: {time_str}")


def main():
    """Run the email processing task in a loop with a delay."""
    while True:
        log_current_time()
        process_emails()
        time.sleep(300)  # Wait for 5 minutes (300 seconds)


if __name__ == '__main__':
    main()
