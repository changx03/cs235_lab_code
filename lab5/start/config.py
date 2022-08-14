from os import environ

from dotenv import load_dotenv

# Load environment variables from `.env`;
load_dotenv()


class DevConfig:
    """Flask configuration for development. Load variables from `.env`;"""
    FLASK_APP = environ.get('FLASK_APP')
    # Task 1: Add your code here
