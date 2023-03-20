import os

from dotenv import load_dotenv

load_dotenv()

ENV = "development"
DEBUG = os.environ.get("DEBUG")
SECRET_KEY = os.environ.get("SECRET_KEY")
