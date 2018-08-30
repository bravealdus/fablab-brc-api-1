from app import db

class Attendace(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    date       = db.Column(db.DateTime, default=db.func.current_timestamp())
    project_title = db.Column(db.String(600), unique=False, nullable=True)
    user_email = db.Column(db.String(600), unique=False, nullable=True)
    project_status = db.Column(db.String(600), unique=False, nullable=True)

    def __repr__(self):
        return '<Asistencia {0} {1}>'.format(self.date, self.user_email, self.project_title)


