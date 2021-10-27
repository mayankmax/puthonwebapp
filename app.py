from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello , World! my name is mayank and i m using app serices in azure"
