from flask import request, jsonify
from app import app, db


@app.route('/flask-runs')
def index():
    return 'Yes it is!'


@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
	res = request.args
	return jsonify(res)
