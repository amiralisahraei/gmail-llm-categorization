# Gmail Categorization Pipeline

This project automates the categorization of Gmail messages using a machine learning model. The pipeline is containerized using Docker for easy deployment and reproducibility.

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
This project extracts emails from Gmail, processes them using a large language model (LLM), categorizes them, and saves the results into a structured CSV file.

## Features
- Extracts emails using the Gmail API
- Processes and categorizes emails using an LLM model
- Saves categorized data into a CSV file
- Containerized using Docker for seamless deployment

## Prerequisites
- Docker installed on your system
- Gmail API credentials (OAuth 2.0)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Set up Gmail API credentials:
   - Follow the [Gmail API setup guide](https://developers.google.com/gmail/api/quickstart/python) to generate your credentials.
   - Save the `credentials.json` file inside the project directory.

3. Build the Docker container:
   ```bash
   docker build -t gmail-categorization .
   ```

## Usage
Run the container:
```bash
docker run --rm -v $(pwd):/app gmail-categorization
```
The processed emails will be stored in `output/emails_categorized.csv`.

## Project Structure
```
├── Dockerfile
├── credentials.json
├── src
│   ├── app.py                 # Main application entry point
│   ├── authenticate_gmail.py  # Handles Gmail API authentication
│   ├── dag.py                 # Workflow orchestration (e.g., Airflow DAG)
│   ├── extract.py             # Extracts emails from Gmail
│   ├── load.py                # Saves processed data (e.g., to CSV/database)
│   ├── sentiment_analysis.py  # Analyzes email sentiment (optional)
│   └── transform.py           # Processes/categorizes emails
├── requirements.txt
├── README.md
```

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the [MIT License](LICENSE).