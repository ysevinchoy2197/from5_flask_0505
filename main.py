#5-misol
from flask import Flask

app = Flask(__name__)

@app.route('/python')
def python_info():
    return f"Pyhon oson til"


@app.route('/flask')
def flask_info():
    return f"Flask web flamework"
