from flask import Flask, render_template, request, jsonify

# create a Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

# function to upload file
from functions.extension import allowed_file
@app.route('/chat_upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if allowed_file(file):
        return jsonify({'success': True}), 200
    elif file:
        return jsonify({'success': False, 'error': 'Invalid file extension.'}), 400
    return jsonify({'success': False, 'error': 'No file detected.'}), 400
    
import sys
if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1].lower() not in ('a','b','c'):
        print("Usage: python3 app.py [A|B|C]")
        sys.exit(1)
    mode = sys.argv[1].lower()
    if mode == 'a':
        # insert code here
        
        # run the app
        app.run()

    elif mode == 'b':
        pass

    elif mode == 'c':
        pass
