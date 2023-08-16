import os 
import redis 
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = ':\xc9K\x96\x03\xf0\xa4\x12"\xe7=#\xfb\xb1nC(\xe7M\xd0\x080<\xcf'

    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:s7FZcQV5ETLUk0u@gradetrack-db.flycast:5432' or\
        #os.environ.get('DATABASE_URL')
    #SESSION_REDIS = redis.from_url("redis://default:8ae7eb3a9e494687872e669601a0a575@fly-gradecalc.upstash.io")
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:postgres@localhost/note_nugget'
    SESSION_REDIS = redis.from_url("redis://localhost:6379")

    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True} 

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True  #sign the session cookie sid