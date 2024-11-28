from flask import Flask, render_template, request, send_file
import mysql.connector
import pandas as pd
from io import BytesIO  # Import BytesIO instead of StringIO

app = Flask(__name__)

# MySQL connection setup
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',  # Use your MySQL password here
        database='classicmodels'
    )
    return connection

# Home route to render the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the search functionality
@app.route('/search', methods=['POST'])
def search():
    search_value = request.form.get('search_value')
    selected_column = request.form.get('column')

    # Query the database based on user input
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = f"SELECT * FROM employees WHERE {selected_column} LIKE %s"
    cursor.execute(query, (f"{search_value}%",))
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    # Return the results to the user
    return render_template('index.html', results=results, search_value=search_value, selected_column=selected_column)

# Route to download the search results as CSV
@app.route('/download', methods=['POST'])
def download():
    search_value = request.form.get('search_value')
    selected_column = request.form.get('column')

    # Query the database based on user input
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = f"SELECT * FROM employees WHERE {selected_column} LIKE %s"
    cursor.execute(query, (f"{search_value}%",))
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    # Convert results to a pandas DataFrame
    df = pd.DataFrame(results)

    # Save DataFrame to a CSV in-memory using BytesIO
    output = BytesIO()  # Use BytesIO for binary data
    df.to_csv(output, index=False)
    output.seek(0)

    # Send the CSV file to the user for download
    return send_file(output, mimetype='text/csv', as_attachment=True, download_name="search_results.csv")

if __name__ == '__main__':
    app.run(debug=True)