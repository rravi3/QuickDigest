from flask import request, abort, session
from flask.json import jsonify 
from app import fc_app, db
from app import bcrypt
from app.models import User
import sys
from user_agents import parse
import openai

#makes sure to check which browser the https request is arriving from to configure appropriately
def checkBrowser():
    user_agent_string = request.headers.get('User-Agent')
    user_agent = parse(user_agent_string)
    print(user_agent.browser.family)
    if user_agent.browser.family == 'PostmanRuntime':
        return
    elif user_agent.browser.family == 'Safari':
        fc_app.config['SESSION_COOKIE_SECURE'] = False
        fc_app.config['SESSION_COOKIE_SAMESITE'] = "Strict"
    else:
        fc_app.config['SESSION_COOKIE_SECURE'] = True
        fc_app.config['SESSION_COOKIE_SAMESITE'] = "None"

    return

@fc_app.route('/register', methods=['POST'])
def register():
    checkBrowser()
    email = request.json.get("email", None)

    password = request.json.get('password', None)

    user_exists = User.query.filter_by(email=email).first() is not None
    
    if user_exists:
        return jsonify({"error": "Unauthorized"}),409
    
    new_user = User(email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    session["user_id"] = new_user.id


    return jsonify({
        "id": new_user.id,
        "email": new_user.email 
    })

@fc_app.route('/@me')
def get_current_user():
    checkBrowser()
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error":"Unauthorized"}),401

    user = User.query.filter_by(id=user_id).first()

    return jsonify({
        "id": user.id,
        "email": user.email 
    })

@fc_app.route('/correct-user',methods=['GET'])
def correctUser():
    checkBrowser()
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error":"Unauthorized"}),401

    
    return jsonify({
        "uid":user_id
    })


@fc_app.route('/get-all-users')
def get_all_users():
    users = User.query.all()

    return jsonify(json_list=[i.serialize for i in users])

@fc_app.route('/delete-all-users',methods=['POST'])
def removeAllUsers():
    checkBrowser()
    all_users = User.query.all()
    
    if all_users is None:
        return jsonify({"error": "Unauthorized"}),409

    for i in all_users:
        db.session.delete(i)
        db.session.commit()

    return "200"
    
@fc_app.route('/login', methods=['POST'])
def login():
    checkBrowser()
    email = request.json.get("email", None)
    password = request.json.get('password', None)

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error":"Unauthorized"}),401

    if not user.check_password(password):
        return jsonify({"error":"Unauthorized"}),401

    session["user_id"] = user.id

    return jsonify({
        "id": user.id,
        "email": user.email 
    })

@fc_app.route('/logout', methods=["POST"])
def logout():
    checkBrowser()
    session.pop("user_id")
    return "200"

# @fc_app.route("/prompt", methods=("GET", "POST"))
# def index():
#     completion = openai.ChatCompletion.create(model="text-davinci-003", prompt="Hello world")
#     return jsonify({
#         "result":completion.choices[0].text
#     })


# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )