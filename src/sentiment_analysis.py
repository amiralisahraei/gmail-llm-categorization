from dotenv import load_dotenv
import os
import re
from langchain_groq import ChatGroq

# Load environment variables from .env file
dotenv_path = "../.env" 
load_dotenv(dotenv_path)

# Access environment variables
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
MODEL_NAME = "deepseek-r1-distill-llama-70b"

# Initialize LLM
def initialize_llm(model_name):
    return ChatGroq(
        model=model_name,
        temperature=0.5,
        max_tokens=None,
        timeout=None,
        streaming=True,
    )

llm = initialize_llm(MODEL_NAME)

SYSTEM_ROLE = """
You are an intelligent assistant designed to help me process and understand the content of my emails. 
Your primary task is to analyze the content of the email and identify its nature. 
For emails related to job applications, determine if the outcome is positive or negative and respond with "Positive" or "Negative". 
For all other types of emails, simply label the result as "Other".
Please ensure that your response is clear and concise, reflecting the nature of the email.
"""

def model_response(message, model_name="deepseek-r1-distill-llama-70b"):
    messages = [
        ("system", SYSTEM_ROLE),
        ("human", message),
    ]
    llm = initialize_llm(model_name)
    output = llm.invoke(messages).content
    # Remove the "thinking" part from response
    output = re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL).strip()
    return output

if __name__ == "__main__":
    message = """
    Amirali,

    We appreciate your interest in working at Aristocrat Interactive. Unfortunately, we will not be moving forward with your application for Data Engineer (ID: R0016773) role.

    We encourage you to follow us on LinkedIn so that when other opportunities arise that align with your background and qualifications, you can be among the first to know.

    If you have applied for more than one role, your resume will be reviewed against those position requirements and applicants, and you will be notified separately regarding the outcome.

    We appreciate your passion for Aristocrat Interactive and wish you the best in your job search.

    Thank you, 
    """

    print(model_response(MODEL_NAME, message))
