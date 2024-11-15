import os
from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection details
DB_HOST = 'localhost'
DB_USER = 'root'        # your MySQL username
DB_PASSWORD = 'root'  # your MySQL password
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

# Home route (index page with file upload form)
@app.route('/')
def index():
    return render_template('index.html')

# Upload route - handles the image upload
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)

    if file:
        # Read the image file as binary
        image_data = file.read()

        # Insert image into the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO images (name, image) VALUES (%s, %s)", 
                       (file.filename, image_data))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
