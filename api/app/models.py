from app import db
from flask_bcrypt import generate_password_hash
from flask_bcrypt import check_password_hash
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(db.Model,Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'user.id'         : self.id,
           'email'         : self.email
       }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)