from app import db

class Attendace(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    date       = db.Column(db.DateTime, default=db.func.current_timestamp())
    project_title = db.Column(db.String(600), unique=False, nullable=True)
    user_email = db.Column(db.String(600), unique=False, nullable=True)
    project_status = db.Column(db.String(600), unique=False, nullable=True)


    def tojson(self):
        return {
           'id': self.id,
           'date': self.date,
           'project_title': self.project_title,
           'user_email': self.user_email,
           'project_status': self.project_status 
        }

    def __repr__(self):
        return str(self.tojson())


