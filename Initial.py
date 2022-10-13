
from flask import Flask

app = Flask(__name__)

@app.route("/")


#Initial Python Script
def hello_world():
	return "Hello world!"