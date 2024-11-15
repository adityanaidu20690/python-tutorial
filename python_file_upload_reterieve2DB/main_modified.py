import os
from flask import Flask, request, render_template, redirect, url_for, flash, send_file
import mysql.connector
from datetime import datetime  # Import datetime for timestamp
from io import BytesIO  # To convert the image binary data into a file-like object

app = Flask(__name__)

# Set a secret key for session management (required for flash messages)
app.secret_key = 'your_secret_key_here'

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
        flash('No file selected. Please choose a file to upload.', 'error')
        return redirect(url_for('index'))
    
    # Read the image file as binary
    image_data = file.read()

    # Get the current date and time
    upload_time = datetime.now()

    # Insert image along with name, Aadhaar, and the upload time into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO images (name, aadhaar, image, upload_time) VALUES (%s, %s, %s, %s)", 
        (name, aadhaar, image_data, upload_time)
    )
    conn.commit()
    cursor.close()
    conn.close()

    flash('Image uploaded successfully!', 'success')
    return redirect(url_for('index'))

# Route to download the image based on name and Aadhaar number
@app.route('/download_image', methods=['POST'])
def download_image():
    name = request.form['name']
    aadhaar = request.form['aadhaar']

    # Server-side validation for Aadhaar number (12 digits)
    if len(aadhaar) != 12 or not aadhaar.isdigit():
        return "Invalid Aadhaar number. Please ensure it is exactly 12 digits.", 400

    # Query the database for the image
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT image FROM images WHERE name = %s AND aadhaar = %s", 
        (name, aadhaar)
    )
    result = cursor.fetchone()

    if result:
        # The image is in binary format, so we need to convert it into a file-like object
        image_data = result[0]
        return send_file(BytesIO(image_data), mimetype='image/jpeg', as_attachment=True, download_name="downloaded_image.jpg")
    else:
        flash("No image found for the provided name and Aadhaar number.", "error")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
