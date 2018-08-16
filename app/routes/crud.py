from flask import request, jsonify
from app import app, db, User, Attendace, Project


@app.route('/')
def index():
    return 'Yes, it works!'


@app.route('/create-project', methods=['GET', 'POST'])
def create_prject():
	args = request.get_json() if request.is_json else request.args
	is_present = Project.query.filter_by(title=args['title']).first()
	if is_present is None:
		project = Project(
			title=args['title'], 
			description=args['description']
		)
		db.session.add(project)
		db.session.commit()
	res = {
		'operation': 'create_prject',
		'args': args, 
		'Host': request.headers['Host'],
	}
	return jsonify(res)


@app.route('/attend', methods=['GET', 'POST'])
def attend():
	args = request.get_json() if request.is_json else request.args
	attendace = Attendace(
		date=args['date'],
		project_id=args['project_id'],
		user_id=args['user_id'],
	)
	db.session.add(attendace)
	db.session.commit()
	res = {
		'operation': 'attend',
		'args': args, 
		'Host': request.headers['Host'],
	}
	return jsonify(res)

	      
@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
	args = request.get_json() if request.is_json else request.args
	is_present = User.query.filter_by(email=args['email']).first()
	if is_present is None:
		me = User(
			role=args['role'], 
			name=args['name'], 
			email=args['email'],
			password=args['password']
		)
		db.session.add(me)
		db.session.commit()
	res = {
		'operation': 'create_user',
		'args': args, 
		'Host': request.headers['Host'],
	}
	return jsonify(res)
