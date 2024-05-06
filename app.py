from flask import Flask, request, render_template
import re

app = Flask(__name__)

import re

def validate_taiwan_id(id_number):
    # Check if ID number is 10 characters long
    if len(id_number) != 10:
        return False

    # Check if the first character is an English letter
    if not id_number[0].isalpha():
        return False

    # Check if the rest of the characters are digits
    if not id_number[1:].isdigit():
        return False

    return True

# 測試
id_number = "A123456789"
if validate_taiwan_id(id_number):
    print("身分證號碼正確")
else:
    print("身分證號碼不正確")


@app.route('/')
def form():
    return render_template('input_data.html')

<html>
<head>
    <title>Input Data</title>
    <style>
        body {
            background-color: lightgrey; /* 背景色設定為淺灰色 */
        }
    </style>
</head>
<body>

@app.route('/submit_form', methods=['POST'])
def handle_form():
    id_number = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    email = request.form.get('email')

    # Validate ID number using the custom function
    if not validate_taiwan_id(id_number):
        return "Invalid Taiwan ID number", 400

    # Validate name (assuming it's alphabetic)
    if not re.match(r'^[A-Za-z\s]+$', name):
        return "Invalid name", 400

    # Validate gender
    if gender not in ['Male', 'Female']:
        return "Invalid gender", 400

    # Validate email
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return "Invalid email", 400

    return "All entries are valid", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Listen on all available network interfaces and port 80

