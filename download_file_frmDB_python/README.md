Project Description: Employee Search and CSV Export Web Application using Flask and MySQL
This project demonstrates a Python web application using Flask, which allows users to search for employee data in a MySQL database (classicmodels). Users can search across multiple columns of the employees table and view the results directly on the frontend. In addition to the search feature, the application allows the user to download the search results as a CSV file.

Technologies Used:
Flask: A micro web framework for Python used to build the web application.
MySQL: Relational database management system used to store employee data.
HTML/CSS: Used for building the frontend user interface.
Pandas: A Python library for data manipulation, used to convert the query results into a CSV file.
Features:
Employee Search:

The application allows users to search employees based on several attributes: First Name, Last Name, Job Title, and Email.
The user types a search term in a text box, and the application fetches the results from the database that match the term across any of the selected columns.
The results are displayed in a tabular format on the webpage.
CSV Download:

After searching, the user can download the search results in the form of a CSV file. The CSV file will contain employee details such as Employee Number, First Name, Last Name, Job Title, and Email.