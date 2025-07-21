from flask import Flask, render_template, request, jsonify

# create a Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

# function to upload file
from functions.extension import ALLOWED_EXTENSIONS, retrieve_extension
from functions.driver import process_driver
@app.route('/chat_upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    exte = retrieve_extension(file.filename)
    if exte in ALLOWED_EXTENSIONS:
        process_driver(exte)
        return jsonify({'success': True}), 200
    elif file:
        return jsonify({'success': False, 'error': 'Invalid file extension.'}), 400
    return jsonify({'success': False, 'error': 'No file detected.'}), 400
    
import sys
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python3 app.py")
        sys.exit(1)

    # run the app
    app.run()
