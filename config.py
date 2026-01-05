import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

# Global Configuration Variables
EMAIL_USER = os.getenv('MAILTRAP_USER')
EMAIL_PASS = os.getenv('MAILTRAP_PASS')
EMAIL_HOST = os.getenv('MAILTRAP_HOST')

# You can also add other global settings here
QUARANTINE_DIR = "./quarantine"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB