import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables
api_key = os.getenv('API_KEY')
# database_url = os.getenv('DATABASE_URL')

print(api_key)
# print(database_url)