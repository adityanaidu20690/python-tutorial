import os
from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
import mysql.connector
from datetime import datetime  # Import datetime for timestamp

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

# Home route (index page with form for entering name and Aadhaar number)
@app.route('/')
def index():
    return render_template('index.html')

# Route to display the list of uploaded images
@app.route('/images')
def view_images():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, aadhaar, image_path, upload_time FROM images")
    images = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('view_images.html', images=images)

# Route to handle step 2, displaying image upload form
@app.route('/step2', methods=['POST'])
def step2():
    # Get the user data from step 1
    name = request.form['name']
    aadhaar = request.form['aadhaar']
    
    # Pass the data to the upload page
    return render_template('upload_image.html', name=name, aadhaar=aadhaar)

# Route to handle image upload
@app.route('/upload', methods=['POST'])
def upload_image():
    # Get the name and Aadhaar number from hidden input fields
    name = request.form['name']
    aadhaar = request.form['aadhaar']

    # Get the file from the form
    file = request.files['file']

    if 'file' not in request.files or file.filename == '':
        flash('No file selected. Please choose a file to upload.', 'error')
        return redirect(url_for('step2'))

    # Ensure the filename is safe and unique (to avoid overwriting)
    filename = file.filename
    filename = filename.replace(" ", "_")  # Replace spaces with underscores
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    # Save the image to the file system
    file.save(file_path)

    # Get the current date and time
    upload_time = datetime.now()

    # Insert name, Aadhaar, and file path into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO images (name, aadhaar, image_path, upload_time) VALUES (%s, %s, %s, %s)",
        (name, aadhaar, filename, upload_time)  # Storing only the filename in the DB, not full path
    )
    conn.commit()
    cursor.close()
    conn.close()

    flash('Image uploaded successfully!', 'success')
    return redirect(url_for('view_images'))

# Route to download an image
@app.route('/download/<int:image_id>')
def download_image(image_id):
    # Connect to the database and fetch the image path based on image_id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT image_path FROM images WHERE id = %s", (image_id,))
    image = cursor.fetchone()
    cursor.close()
    conn.close()

    if image is None:
        flash('Image not found.', 'error')
        return redirect(url_for('index'))

    # Extract the image file path from the database record
    image_path = image[0]

    # Ensure the file exists
    if not os.path.exists(os.path.join(UPLOAD_FOLDER, image_path)):
        flash('Image file not found on the server.', 'error')
        return redirect(url_for('index'))

    # Serve the image file for download
    return send_from_directory(UPLOAD_FOLDER, image_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
