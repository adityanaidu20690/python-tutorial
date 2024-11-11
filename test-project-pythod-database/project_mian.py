from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask( __name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/employee_details'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/employee_details'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turn off modification tracking
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
#     'connect_args': {
#         'ssl': {'disabled': True}
#     }
# }

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:@localhost/employee_details?ssl_mode=DISABLED'


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/employee_details?ssl_disabled=True'
db = SQLAlchemy(app)

class employee(db.Model):
    # Sno , Name , Email_ID , Contact_no , Joining_Date
    sno= db.Column(db.Integer , primary_key=True, autoincrement=True)
    Name= db.Column(db.String(80) ,  nullable=False)
    Email_ID= db.Column(db.String(120) , nullable=False)
    Contact_no= db.Column(db.String(20) , nullable=False)

@app.route("/searching", methods=["GET"])
def searching():
    # print("Search route accessed!")
    employees = employee.query.all()  # Fetch all records from the employee table
    return render_template("employee_list.html", employees=employees)  # Pass data to the template

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        name = request.form.get('name')  # Get the name from the form
        if name:
            # Query by 'Name' (with capital 'N') because that's how the column is defined
            # employee_data = employee.query.filter_by(Name=name).first()
            employee_data=employee.query.filter_by(Name=name).first()  # Fetch the employee by their name
            if employee_data:
                return render_template("search.html", employee=employee_data)  # Show employee details
            else:
                message = "No employee found with that name"
                return render_template("search", message=message)  # Show message on the search page
    return render_template("search.html")  # Show the search form initially


@app.route("/contact", methods=['GET', 'POST'])
def addy():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        contact_no = request.form.get('contact_no')

        # Creating a new entry for the employee table
        entry = employee(Name=name, Email_ID=email, Contact_no=contact_no)
        
        try:
            # Adding and committing the entry to the database
            db.session.add(entry)
            db.session.commit()
            message = "Employee details added successfully!"
        except Exception as e:
            db.session.rollback()
            message = f"An error occurred: {str(e)}"

        # Passing the message to the template
        return render_template('test_contactUS.html', message=message)
    
    return render_template('test_contactUS.html')
with app.app_context():
    db.create_all()

# if __name__ == '__main__':
#     app.run(debug=True)
app.run(debug=True)