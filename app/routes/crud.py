from flask import request, jsonify
from app import app, db, User, Attendace, Project
from datetime import date, datetime

@app.route('/')
def index():
    return 'Yes, it works!'


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
    		'results': {},
    		'code': 404,
    		'error': 'page not found'
    	})


@app.route('/create-project', methods=['GET', 'POST'])
def create_prject():
	args = request.get_json() if request.is_json else request.args
	is_present = Project.query.filter_by(title=args['title']).first()
	if is_present is None:
		owner = User.query.filter_by(id=args['participants'][0]).first()
		project = Project(
			title=args['title'], 
			description=args['description']
		)
		owner.projects.append(project)
		db.session.add_all([project, owner])
		db.session.commit()
	res = {
		'new entry?': is_present == None,
		'operation': 'create_prject',
		'args': args, 
		'Host': request.headers['Host'],
	}
	return jsonify(res)


@app.route('/check-in', methods=['GET', 'POST'])
def check_in():
	args = request.get_json() if request.is_json else request.args
	last_checkin = (Attendace.query
					.filter_by(user_email=args['user_email'])
					.order_by(Attendace.id.desc())
					.first())
	
	already_done = True
	if last_checkin is None or last_checkin.date.date() < date.today():
		already_done = False
		attendace = Attendace(
			user_email=args['user_email'],
			project_title=args['project_title'],
			project_status=args['project_status']
		)
		db.session.add(attendace)
		db.session.commit()

	res = {
		'operation': 'check_in',
		'args': args, 
		'Host': request.headers['Host'],
		'result': {
			'date': last_checkin.date if last_checkin else datetime.now(),
			'already': already_done
			
		}
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


@app.route('/user', methods=['GET'])
def user():
	args = request.get_json() if request.is_json else request.args
	db_res = User.query.filter_by(email=args['email']).first()
	return jsonify({
			'Host': request.headers['Host'],
			'args': args,
			'result': db_res.tojson() if db_res else False
		})


@app.route('/projects', methods=['GET'])
def projects():
	args = request.get_json() if request.is_json else request.args
	db_res = User.query.filter_by(id=args['user']).first()
	return jsonify({
			'Host': request.headers['Host'],
			'args': args,
			'result': db_res.tojson()
			# 'result': [dict(user.tojson()) for user in db_res]
		})


@app.route('/all-users', methods=['GET'])
def all_users():
	args = request.get_json() if request.is_json else request.args
	db_res = User.query.all()
	return jsonify({
			'Host': request.headers['Host'],
			'args': args,
			'result': [dict(user.tojson()) for user in db_res]
		})
	


@app.route('/all-projects', methods=['GET'])
def all_projects():
	args = request.get_json() if request.is_json else request.args
	db_res = Project.query.all()
	return jsonify({
			'Host': request.headers['Host'],
			'args': args,
			'result': [dict(project.tojson()) for project in db_res]
		})
	

