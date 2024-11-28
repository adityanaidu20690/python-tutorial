from flask import Flask, request, render_template, flash, send_from_directory, redirect, url_for
import os
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Set a secret key for session management (required for flash messages)
app.secret_key = 'your_secret_key_here'

# MySQL connection details
DB_HOST = 'localhost'
DB_USER = 'root'        # your MySQL username
DB_PASSWORD = 'root'    # your MySQL password
DB_NAME = 'image_upload_db'  # your database name

# Directory to store uploaded images
UPLOAD_FOLDER = 'uploads'  # Define the folder to save images
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the directory if it doesn't exist

# Connect to MySQL database
def get_db_connection():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection

# Route to view an image in the browser
@app.route('/view/<int:image_id>')
def view_image(image_id):
    # Fetch the image path from the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT image_path FROM images WHERE id = %s", (image_id,))
    image = cursor.fetchone()
    cursor.close()
    conn.close()

    if image is None:
        flash('Image not found.', 'error')
        return redirect(url_for('index'))

    # Return the image for viewing in the browser
    image_path = image[0]
    return send_from_directory(UPLOAD_FOLDER, image_path)

# Home route (index page with form for entering name and Aadhaar number)
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    aadhaar = None
    uploaded_files = []

    if request.method == 'POST':
        name = request.form['name']
        aadhaar = request.form['aadhaar']

        # Validate Aadhaar number to ensure it's exactly 12 digits
        if len(aadhaar) != 12 or not aadhaar.isdigit():
            flash("Aadhaar number must be exactly 12 digits.", 'error')
            return render_template('index.html', name=name, aadhaar=aadhaar)

        # Fetch uploaded files for this name and Aadhaar
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, aadhaar, image_path, upload_time FROM images WHERE aadhaar = %s", (aadhaar,))
        uploaded_files = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('index.html', name=name, aadhaar=aadhaar, uploaded_files=uploaded_files)

    return render_template('index.html', active_tab='step1')


# Route to handle image upload and saving to database
@app.route('/upload', methods=['POST'])
def upload_image():
    # Get name and Aadhaar number from the form
    name = request.form['name']
    aadhaar = request.form['aadhaar']
    
    # Get the file from the form
    file = request.files['document']

    if 'document' not in request.files or file.filename == '':
        flash('No file selected. Please choose a file to upload.', 'error')
        return redirect(url_for('index'))

    # Check if the Aadhaar number already has a record in the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM images WHERE aadhaar = %s", (aadhaar,))
    existing_entries = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    if existing_entries > 0:
        flash('A file has already been uploaded for this Aadhaar number. Duplicate entry is not allowed.', 'error')
        return redirect(url_for('index'))

    # Ensure the filename is safe and unique (to avoid overwriting)
    filename = file.filename
    filename = filename.replace(" ", "_")  # Replace spaces with underscores

    # Ensure the file doesn't already exist in the upload folder
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        # If file exists, generate a unique filename by adding timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{filename}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)

    # Save the file to the upload folder
    file.save(file_path)

    # Get the current date and time for timestamp
    upload_time = datetime.now()

    # Insert the data into the MySQL database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO images (name, aadhaar, image_path, upload_time) VALUES (%s, %s, %s, %s)",
        (name, aadhaar, filename, upload_time)
    )
    conn.commit()
    cursor.close()
    conn.close()

    flash('Document uploaded successfully!', 'success')

    # After uploading, fetch the uploaded documents and display them on the same page
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, aadhaar, image_path, upload_time FROM images WHERE aadhaar = %s", (aadhaar,))
    uploaded_files = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', name=name, aadhaar=aadhaar, uploaded_files=uploaded_files)

# Route to download a file
@app.route('/download/<int:image_id>')
def download_image(image_id):
    # Fetch the image path from the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT image_path FROM images WHERE id = %s", (image_id,))
    image = cursor.fetchone()
    cursor.close()
    conn.close()

    if image is None:
        flash('Image not found.', 'error')
        return redirect(url_for('index'))

    # Return the file for download
    image_path = image[0]
    return send_from_directory(UPLOAD_FOLDER, image_path, as_attachment=True)

# Route to fetch all documents
@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    # Fetch all uploaded documents from the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, aadhaar, image_path, upload_time FROM images")
    uploaded_files = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', uploaded_files=uploaded_files)

if __name__ == '__main__':
    app.run(debug=True)
