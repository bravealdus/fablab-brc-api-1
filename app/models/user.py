from app import db

class User(db.Model):
    id       = db.Column(db.Integer, primary_key = True)
    role     = db.Column(db.String(10), unique   = False, nullable = True)
    name     = db.Column(db.String(120), unique  = False, nullable = False)
    email    = db.Column(db.String(120), unique  = True, nullable  = False)
    password = db.Column(db.String(120), unique  = False, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.name