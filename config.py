import os

from dotenv import load_dotenv

load_dotenv()

FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
SECRET_KEY = os.environ.get("SECRET_KEY")
ENV = os.environ.get("ENV")
