import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# DB config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI') or 'postgresql://localhost:5432/fablab-1'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models.all_models import *
from .routes.all_routes import *
