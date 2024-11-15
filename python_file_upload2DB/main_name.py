import os
from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection details
DB_HOST = 'localhost'
DB_USER = 'root'        # your MySQL username
DB_PASSWORD = 'root'    # your MySQL password
DB_NAME = 'image_upload_db'  # your database name

# Connect to MySQL database
def get_db_connection():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection

# Home route (index page with form for entering name and Aadhaar number)
@app.route('/')
def index():
    return render_template('index.html')

# Route to display form for uploading image (after step 1)
@app.route('/step2', methods=['POST'])
def step2():
    name = request.form['name']
    aadhaar = request.form['aadhaar']

    # Server-side validation for Aadhaar number (12 digits)
    if len(aadhaar) != 12 or not aadhaar.isdigit():
        return "Invalid Aadhaar number. Please ensure it is exactly 12 digits.", 400

    # Store name and Aadhaar number in session or pass to next step
    return render_template('upload_image.html', name=name, aadhaar=aadhaar)

# Upload route - handles the image upload
@app.route('/upload', methods=['POST'])
def upload_image():
    name = request.form['name']
    aadhaar = request.form['aadhaar']
    file = request.files['file']
    
    if 'file' not in request.files or file.filename == '':
        return redirect(url_for('index'))
    
    # Read the image file as binary
    image_data = file.read()

    # Insert image along with name and Aadhaar into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (name, aadhaar, image) VALUES (%s, %s, %s)", 
                   (name, aadhaar, image_data))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
