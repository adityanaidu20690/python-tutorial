To create a database named image_upload_db, use the following SQL command:
CREATE DATABASE image_upload_db;

After creating the database, you need to select it in order to create the table. Use the command:
USE image_upload_db;



Now, create the images table with the following structure. This table will store the uploaded image details such as name, Aadhaar number, image file path, and upload time.


CREATE TABLE images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    aadhaar VARCHAR(12),
    image_path VARCHAR(255),  -- Path to the stored image file
    upload_time DATETIME
);
