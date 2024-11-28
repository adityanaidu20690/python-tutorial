Create a Python web application using Flask that allows us to access a local MySQL Workbench database. We will use the classicmodels database with the employees table.

In the frontend (index.html), there should be a text field where users can enter a search term, and beside the field, there should be a dropdown menu with the following options: First Name, Last Name, Employee Number, Job Title, and Email.

When the user selects an option from the dropdown (e.g., First Name), enters a search term (e.g., a letter or part of the name), and clicks the search button, the application will query the database and display all the records related to the search term from the selected column.

Once the search results are displayed, the user should have the option to download the data as a .csv file.