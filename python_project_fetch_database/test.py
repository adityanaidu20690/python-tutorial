from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/employee_details'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class employee(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(80), nullable=False)
    Email_ID = db.Column(db.String(120), nullable=False)
    Contact_no = db.Column(db.String(20), nullable=False)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_letter = request.form.get('name') 
        # search_email = request.form.get('email')
        if search_letter:
            search_letter = search_letter.lower()  
            employees = employee.query.filter(employee.Name.ilike(f"{search_letter}%")).all()
            
            if employees:
                return render_template("search.html", employees=employees, search_letter=search_letter)
            else:
                message = "No employee found with given letter."
                return render_template("search.html", message=message)

    return render_template("search.html")

app.run(debug=True)
    
