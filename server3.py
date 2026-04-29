from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Server 3 OK"

app.run(port=8003)