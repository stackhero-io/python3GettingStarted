import signal, os, sys
import time
from flask import Flask
app = Flask(__name__)

# Define route "/" named "index"
@app.route('/')
def index():
  return '🎉 Congratulations! Your first Python3 application is running on Stackhero!'


# You'll see this log directly on your Stackhero's console
print('🎉 The app has just start!')


# Handle termination signal
# When you will push your new code to Stackhero, we will send a termination signal (SIGTERM) to your running app.
# The goal here is to let your app closing connections properly, like connections to databases etc...
sigtermHandled = False
def sigtermHandler(signum, frame):
  # Avoid to execute multiple time this function
  global sigtermHandled
  if sigtermHandled == True:
    return
  sigtermHandled = True

  # You'll see this log directly on your Stackhero's console
  print('😯 SIGTERM signal received')

  # You can close your database connection and do other cleanup here
  # dbConnection.close()

  # Finally exit the process
  sys.exit(0)

signal.signal(signal.SIGTERM, sigtermHandler)
