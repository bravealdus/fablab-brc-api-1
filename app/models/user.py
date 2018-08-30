from app import db



class User(db.Model):
    id       = db.Column(db.Integer, primary_key = True)
    role     = db.Column(db.String(10), unique   = False, nullable = True)
    name     = db.Column(db.String(120), unique  = False, nullable = False)
    email    = db.Column(db.String(120), unique  = True, nullable  = False)
    password = db.Column(db.String(120), unique  = False, nullable = False)
    # projects = db.relationship('Project', lazy='subquery', backref=db.backref('users', lazy=True))

    def tojson(self):
    	print('\n\n\n\n\n\n\n', self.projects)
    	return {
        	'id': self.id,
        	'role': self.role,    
			'name': self.name,
			'email': self.email,
			'password': self.password,
			# 'projects': [dict(project.tojson()) for project in self.projects]
        }

    def __repr__(self):
        return str(self.tojson())