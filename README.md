# Natural Language to SQL Query Conversion App

This project is a Streamlit-based application that converts natural language queries into SQL queries using Google's Gemini model. It also retrieves and displays results from an SQLite database.

## Project Structure

- **`sql.py`**: Script to set up the SQLite database (`student.db`). It creates a `STUDENT` table and inserts sample records.
- **`app.py`**: The main application script that handles user input, generates SQL queries using the Google Gemini model, and displays the results.
- **`.env`**: Stores the Google API key used for accessing the Gemini model.
- **`requirements.txt`**: Lists all the Python dependencies required to run the project.
- **`student.db`**: The SQLite database that contains the `STUDENT` table with sample data.

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your_username/text_to_sql.git
    cd text_to_sql
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the environment variables**:
   - Create a `.env` file in the root directory and add your Google API key:
     ```plaintext
     GOOGLE_API_KEY = "your_google_api_key_here"
     ```

4. **Set up the SQLite database**:
    - Run the `sql.py` script to create the `student.db` file and insert sample records:
      ```bash
      python sql.py
      ```

5. **Run the Streamlit app**:
    - Start the application using Streamlit:
      ```bash
      streamlit run app.py
      ```

## Usage

- The app allows you to input natural language questions. It uses the Google Gemini model to convert these into SQL queries and retrieves data from the `student.db` SQLite database.
- Example queries:
  - "How many entries of records are present?"
  - "Tell me all the students studying in Data Science class?"

## Files

- **`sql.py`**: Script to set up the `STUDENT` table in the SQLite database.
- **`app.py`**: Streamlit application to interact with the user and process queries.
- **`.env`**: Environment variables file storing sensitive data such as API keys.
- **`requirements.txt`**: Dependency file for easy setup.
- **`student.db`**: SQLite database with pre-populated student records.

## Requirements

- Python 3.x
- Streamlit
- Google Generative AI library (`google-generativeai`)
- Python dotenv (`python-dotenv`)
