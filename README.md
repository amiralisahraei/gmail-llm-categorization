
# Gmail ETL Categorization

This project automates the extraction, transformation, and categorization of Gmail messages using a machine learning model. The ETL pipeline is containerized using Docker for easy deployment and reproducibility.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project follows the ETL (Extract, Transform, Load) pipeline structure to process Gmail emails. It extracts emails using the Gmail API, transforms and categorizes them using a large language model (LLM), and loads the results into a structured CSV file.

## Features
- Extracts emails using the Gmail API
- Transforms and categorizes emails using an LLM model
- Loads categorized data into a CSV file
- Containerized using Docker for seamless deployment

## Prerequisites
- Docker installed on your system
- Gmail API credentials (OAuth 2.0)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/amiralisahraei/gmail-llm-categorization.git
   cd gmail-etl-categorization
   ```

2. Set up Gmail API credentials:
   - Follow the [Gmail API setup guide](https://developers.google.com/gmail/api/quickstart/python) to generate your credentials.
   - Save the `credentials.json` file inside the project directory.

## Usage

### Option 1: Run Using Pre-Built Docker Image from Docker Hub
If you don't want to build the image yourself, you can pull and run the pre-built Docker image from Docker Hub:
```bash
docker run --rm -v $(pwd):/app amiralisahraei/gmail-categorization:latest
```
Make sure to replace `<docker_hub_username>` with the correct Docker Hub username.

### Option 2: Build and Run the Docker Image Locally
If you prefer to build the Docker image locally:
1. Build the Docker container:
   ```bash
   docker build -t gmail-etl-categorization .
   ```

2. Run the Docker container:
   ```bash
   docker run --rm -v $(pwd):/app gmail-etl-categorization
   ```

The processed emails will be stored in `output/emails_categorized.csv`.

### Option 3: Run Without Docker (Directly on Your Local Machine)
If you want to run the project directly on your local machine without Docker:
1. Install the necessary Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Python script:
   ```bash
   python src/app.py
   ```

## Project Structure
```
├── Dockerfile                  # Docker configuration for building the container
├── credentials.json            # Gmail API credentials file
├── src
│   ├── app.py                 # Main application entry point
│   ├── authenticate_gmail.py  # Handles Gmail API authentication
│   ├── extract.py             # Extracts emails from Gmail (ETL - Extract)
│   ├── transform.py           # Processes/categorizes emails (ETL - Transform)
│   ├── load.py                # Saves processed data to CSV/database (ETL - Load)
│   ├── sentiment_analysis.py  # Analyzes email sentiment (optional)
│   ├── dag.py                 # Workflow orchestration for Airflow (if needed)
├── requirements.txt           # List of Python dependencies
├── README.md                  # Project documentation
```

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the [MIT License](LICENSE).