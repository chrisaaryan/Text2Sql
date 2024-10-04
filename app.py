from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Make sure you have set the GOOGLE_API_KEY environment variable correctly.")
    st.stop()

# Configure the API key
genai.configure(api_key=api_key)

# Function to load Google Gemini model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text.strip()

# Function to retrieve query results from the SQL database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.
    \n\nFor example:
    - Example 1: How many entries of records are present? The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
    - Example 2: Tell me all the students studying in Data Science class? The SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS = "Data Science";
    \n\nNote: The SQL code should not have ''' at the beginning or end, and the SQL keyword should not be included in the output.
    """
]

# Creating Streamlit app
st.set_page_config(page_title="I Can Retrieve Any SQL Query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the Question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    if response:
        st.write(f"Generated SQL Query: {response}")
        data = read_sql_query(response, "student.db")
        if data:
            st.subheader("Query Results")
            st.table(data)
        else:
            st.write("No results found or an error occurred.")
    else:
        st.write("No response generated.")
