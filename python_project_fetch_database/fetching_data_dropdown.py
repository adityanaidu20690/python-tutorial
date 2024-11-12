from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/employee_details'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/employee_details'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Employee model (ensure the table name is lowercase if it's explicitly defined)
class employee(db.Model):  # 'Employee' class corresponds to the 'employee' table in the DB
    # __tablename__ = 'employee'  # Explicitly defining the table name in lowercase (optional)
    
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(80), nullable=False)
    Email_ID = db.Column(db.String(120), nullable=False)
    Contact_no = db.Column(db.String(20), nullable=False)

# Search route
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get('query', '')  # Get the search query from the form (GET)
    search_type = request.args.get('search_type', 'name')  # Get the search type from the dropdown
    
    employees = []  # Initialize an empty list for employees

    # Handle POST method for searching by first letter of the name
    if request.method == "POST":
        search_letter = request.form.get('name')
        if search_letter:
            search_letter = search_letter.lower()  
            employees = employee.query.filter(employee.Name.ilike(f"{search_letter}%")).all()

            if employees:
                return render_template("test.html", employees=employees, query=search_letter, search_type='name')
            else:
                message = "No employee found with the given first letter."
                return render_template("test.html", message=message)

    # Handle GET method for different search types based on dropdown selection
    if query:
        if search_type == 'name':
            # Search by Name (case insensitive and partial match)
            employees = employee.query.filter(employee.Name.ilike(f"{query.lower()}%")).all()
        
        elif search_type == 'email':
            # Search by Email ID (case insensitive and partial match)
            employees = employee.query.filter(employee.Email_ID.ilike(f"{query.lower()}%")).all()
        
        elif search_type == 'contact':
            # Search by Contact Number (partial match)
            employees = employee.query.filter(employee.Contact_no.ilike(f"{query}%")).all()
        
        elif search_type == 'sno':
            # Search by S.No (exact match), ensure query is a valid integer
            try:
                sno = int(query)
                employees = employee.query.filter(employee.sno == sno).all()
            except ValueError:
                # Handle case where query is not a valid integer
                employees = []  # No results if invalid sno is entered

    # Render the template with results
    return render_template("test.html", employees=employees, query=query, search_type=search_type)

# Run the application (with __name__ check for best practice)
if __name__ == "__main__":
    app.run(debug=True)
