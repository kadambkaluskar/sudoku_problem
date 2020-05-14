# api/app.py

from flask import Flask
from flask import request
from flask import jsonify
import numpy as np

app = Flask(__name__)

def check_small_cube(index):
	i = 0
	print('inside-function',index)
	for i in range(2,9,3):
		print('i - ',i)
		if 45 != sudoku_list[index-2][i-2] + sudoku_list[index-2][i-1] + sudoku_list[index-2][i]  \
			+ sudoku_list[index-1][i-2] + sudoku_list[index-1][i-1] + sudoku_list[index-1][i] \
			+ sudoku_list[index][i-2]   + sudoku_list[index][i-1]   + sudoku_list[index][i] :
			return True
	return False

def validate_sudoku(input_list):
	is_sudoku_valid = True
	global sudoku_list
	sudoku_list = np.array(input_list).reshape(9,9)
	sudoku_coloumns = list(zip(*sudoku_list))
	for index in range(0,9):
		if (sum(set(sudoku_list[index])) != 45) or (sum(set(sudoku_coloumns[index])) != 45) :
			is_sudoku_valid = False
			break
		if (index+1)%3==0 and check_small_cube(index):
			is_sudoku_valid = False
			break
	return is_sudoku_valid

@app.route('/')
def hello_world():
    return 'Hey, Welcome to Sudoku Validation Problem!'

@app.route('/verify-sudoku', methods=["GET", "POST"])
def verify_sudoku():
    input_list = request.get_json('input')
    input_list = input_list['input']
    if validate_sudoku(input_list) :
    	return jsonify({"result":"true"})
    else :
    	return jsonify({"result" : "False"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')