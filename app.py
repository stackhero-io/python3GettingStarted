from flask import Flask
app = Flask(__name__)

# Define route "/" named "index"
@app.route('/')
def index():
  return '🎉 Congratulations! Your first Python3 application is running on Stackhero!'