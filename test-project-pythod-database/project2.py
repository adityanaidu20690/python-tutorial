from flask import Flask , render_template
app = Flask(__name__)
@app.route ("/")
def ace():
    return render_template("index.html")

@app.route ("/bootstrap")
def addy():
    return render_template("bootstrap.html")
app.run(debug=True)

    