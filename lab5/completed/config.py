from os import environ

from dotenv import load_dotenv

# Load environment variables from `.env`;
load_dotenv()


class DevConfig:
    """Flask configuration for development. Load variables from `.env`;"""
    FLASK_APP = environ.get('FLASK_APP')
    # Task 1: Add your code here
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    FLASK_RUN_HOST = environ.get('FLASK_RUN_HOST')
    FLASK_RUN_PORT = environ.get('FLASK_RUN_PORT')
    SECRET_KEY = environ.get('SECRET_KEY')
    WTF_CSRF_SECRET_KEY = environ.get('WTF_CSRF_SECRET_KEY')
