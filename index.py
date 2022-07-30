from cgitb import text
from flask import Flask


app = Flask(__name__)

@app.route("/")

def home():
    
    return "Hello Mom <h1>TextHere</h1><button>Click ME</button>"

if __name__=="__main__":
    app.run()