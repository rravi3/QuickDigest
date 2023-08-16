from flask import Flask, session
from config import Config
from flask_cors import CORS
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_session import Session

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

fc_app = Flask(__name__)
fc_app.config.from_object(Config)
CORS(fc_app, supports_credentials=True)

bcrypt = Bcrypt(fc_app)
db = SQLAlchemy(fc_app, metadata)
migrate = Migrate(fc_app, db,render_as_batch=True)
server_session = Session(fc_app)

from app import routes, models