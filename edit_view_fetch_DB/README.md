Project Description
Document Upload System

This project is a web-based application designed to manage the upload, viewing, and downloading of documents (such as images or PDFs). It uses Flask as the backend web framework and MySQL for storing information about the uploaded files. The application allows users to:

Enter their name and Aadhaar number: The user can input their personal information, which is validated to ensure the Aadhaar number is exactly 12 digits long.
Upload documents: Once the Aadhaar number is validated, the user can upload a file (image or document). The file is saved to the server, and its information (name, Aadhaar number, file path, and upload time) is stored in the MySQL database.
View uploaded documents: The user can view a list of documents uploaded for their Aadhaar number.
Download documents: The uploaded files can be downloaded at any time by the user.
Fetch all documents: The system can fetch and display a list of all uploaded documents from the database.
The core features of the project include:

Form Validation: Ensures that the Aadhaar number is correctly formatted (12 digits).
File Upload: Supports image and document uploads, with proper checks to prevent duplicate submissions.
Database Integration: Uses MySQL to store details about the uploaded files and their associated users.
Flask Routing: Uses Flask's routing system to handle various routes such as viewing, uploading, and downloading files.
The application supports basic file operations like uploading, viewing, downloading, and displaying uploaded files in an interactive table.