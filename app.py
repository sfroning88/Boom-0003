from flask import Flask, render_template, request, jsonify

# create a Flask app
app = Flask(__name__)

@app.route('/')
def home():
    global timeout_occurred
    if timeout_occurred:
        # Reset the timeout flag when accessing the home page
        timeout_occurred = False
    
    return render_template('chat.html')
