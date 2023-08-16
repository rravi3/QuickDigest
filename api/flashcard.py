from app import fc_app,db   
from app.models import User

@fc_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}