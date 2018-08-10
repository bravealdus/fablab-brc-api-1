from flask import request, jsonify
from app import app, db


@app.route('/')
def index():
    return 'Yes, it works!'


@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
	res = request.args
	return jsonify(res)
