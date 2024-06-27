# Real-time Sentiment Analysis on Cryptocurrency Market Trends

## Overview
Constructed a real-time system to ingest and preprocess data from Twitter and Google News, achieving 91% accuracy with NLTK’s VADER and fine-tuned BERT Transformer. Deployed dashboards for visualization and used AWS S3 for storage.

## Tech Stack
- AWS (SageMaker, Kinesis)
- Apache Kafka
- NLTK
- BERT Transformer

## Setup Instructions
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/crypto-sentiment-analysis.git
    cd crypto-sentiment-analysis
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure AWS and create necessary services (S3 bucket, SageMaker notebook, Kinesis stream).

## Running the Project
1. Run data ingestion scripts:
    ```sh
    python data_ingestion/twitter_streaming.py
    python data_ingestion/google_news_scraper.py
    ```

2. Run data preprocessing script:
    ```sh
    python data_preprocessing/preprocessing.py
    ```

3. Start the Flask dashboard:
    ```sh
    python dashboard/app.py
    ```

4. Deploy the model to AWS SageMaker:
    ```sh
    python deployment/aws_sagemaker_deploy.py
    ```

## Usage
Access the dashboard at `http://localhost:5000` to view real-time sentiment analysis of cryptocurrency trends.
