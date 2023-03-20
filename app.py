from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

print(f"The app environment is: {app.config.get('ENV')}")
print(f"Debug is set to: {app.config.get('DEBUG')}")
print(f"The secret key is: {app.config.get('SECRET_KEY')}")

