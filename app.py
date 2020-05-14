# api/app.py

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, Welcome to Sudoku Problem!'







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
