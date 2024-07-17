# app.py

from flask import Flask, render_template, request, jsonify
import os
from main import main  # Import the main function

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract_data', methods=['POST'])
def extract_data():
    file = request.files['file']
    new_file = file.filename
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], new_file)
    file.save(pdf_path)

    # Call the main function directly
    result = main(pdf_path)
    
    # Return the result as JSON
    return jsonify({'tax-amount': result})

if __name__ == '__main__':
    app.run(debug=True)
