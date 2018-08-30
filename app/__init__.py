import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


# DB config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL') or 'postgresql://localhost:5432/fablab-1'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models.all_models import *
from .routes.all_routes import *
