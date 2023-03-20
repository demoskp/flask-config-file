from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

print(f"Debug is set to: {app.config.get('DEBUG')}")
print(f"Secret key is: {app.config.get('SECRET_KEY')}")
print(f"The environment is: {app.config.get('ENV')}")
