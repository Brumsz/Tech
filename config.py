import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(find_dotenv)

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET = os.getenv('SECRET')