from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

print(f"Debug is: {app.config.get('FLASK_DEBUG')}")
print(f"Secret key is: {app.config.get('SECRET_KEY')}")
print(f"Environment is: {app.config.get('ENV')}")
