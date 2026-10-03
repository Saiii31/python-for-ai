import os
from dotenv import load_dotenv

load_dotenv(".env")  # Load environment variables from .env file

# Access environment variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
print(f"API Key: {api_key}")
print(f"Database URL: {database_url}")