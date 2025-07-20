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

# handle to send chat requests
@app.route("/get", methods=["GET", "POST"])
def send_chat():
    msg = request.form["msg"]
    input = msg
    return get_response(input)

# function to get response
def get_response(prompt):
    output = 'Flask app is working.'
    return f'{prompt} -> {output}'

# function to upload file
@app.route('/chat_upload', methods=['POST'])
def upload_file():
    msg = request.form.get('msg', '')
    file = request.files.get('file')
    if file:
        return jsonify({'success': True}), 200
    return get_response(msg)

import sys
if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1].lower() not in ('a','b','c'):
        print("Usage: python3 app.py [A|B|C]")
        sys.exit(1)
    mode = sys.argv[1].lower()
    if mode == 'a':
        # run the app
        app.run()

    elif mode == 'b':
        pass

    elif mode == 'c':
        pass
