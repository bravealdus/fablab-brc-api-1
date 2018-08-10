from app import db

participants = db.Table('user_project',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True)
)

class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120), unique=False, nullable=False)
	description = db.Column(db.String(600), unique=False, nullable=True)
	participants = db.relationship('User', secondary=participants, lazy='subquery', backref=db.backref('projects', lazy=True))




