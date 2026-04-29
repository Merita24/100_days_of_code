from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Server 2 OK"

app.run(port=8002)