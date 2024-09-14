# Intrusion Detection System

This project implements a simple Intrusion Detection System (IDS) using machine learning. It allows users to upload CSV files containing network traffic data and checks for potential attacks.

## Setup

1. Clone this repository.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Train the model (make sure you have the dataset):
   ```
   python model/train_model.py
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage

1. Open the Streamlit app in your web browser.
2. Upload a CSV file containing network traffic data.
3. Click the "Check for Attacks" button to analyze the data.
4. View the results, including the percentage of detected attacks and a sample of attack records.

## File Structure

- `app.py`: Main Streamlit application
- `preprocessing/preprocess.py`: Data preprocessing functions
- `utils/helpers.py`: Utility functions
- `model/train_model.py`: Script for training the machine learning model
- `model/model.joblib`: Saved machine learning model (generated after training)
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation

## Note

Make sure to train the model with your specific dataset before using the application. Adjust the preprocessing steps and model parameters as needed for your use case.
