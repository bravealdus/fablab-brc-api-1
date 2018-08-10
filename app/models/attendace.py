from app import db

class Attendace(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    date       = db.Column(db.DateTime, default=db.func.current_timestamp())
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)
    project    = db.relationship('Project', backref=db.backref('projects', lazy=True))
    user_id    = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user       = db.relationship('User', backref=db.backref('attendaces', lazy=True))

    def __repr__(self):
        return '<Asistencia {0} {1}>'.format(self.date, self.user.name)


