from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route("/")
def hello():
    return render_template("index.html")
    # return "Death is the new beginning!!"
@app.route("/about")
def addy():
    name= "Goku"
    return render_template("about.html", name2= name)
app.run(debug=True)