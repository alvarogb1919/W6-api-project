from flask import Flask, request
from flask import jsonify
from pandas.core.accessor import DirNamesMixin

# Importamos nuestros módulos de funciones
import tools.getdata as get 
import tools.postdata as pos

app = Flask(__name__)

# INDEX

@app.route("/")
def index():
    return "Welcome to The Office chat API!"

# GET QUERIES

@app.route("/users")
def users():
    users = get.users_list()
    return jsonify(users)

@app.route("/groups")
def groups():
    groups = get.groups_list()
    return jsonify(groups)

@app.route("/messages")
def messages():
    messages = get.message_list()
    return jsonify(messages)

@app.route("/group_messages/<group_id>")
def chat_messages(group_id):
    group_messages = get.messages_group(group_id)
    return jsonify(group_messages)

@app.route("/user_messages/<user_id>")
def user_messages(user_id):
    user_messages = get.messages_user(user_id)
    return jsonify(user_messages)

# POST QUERIES

@app.route("/new_message", methods=["POST"])
def insert_message():
    message = request.form.get("message")
    user = request.form.get("user_id")
    group = request.form.get("group_id")
    pos.insert_message(message, user, group)
    return "Message has been correctly inserted"

@app.route("/new_group", methods=["POST"])
def insert_group():
    grupo = request.form.get("group_number")
    pos.create_group(grupo)
    return "Group has been correctly created"

@app.route("/new_user_in_chat", methods=["POST"])
def insert_user_in_chat():
    user = request.form.get("user_id")
    grupo = request.form.get("group_id")
    pos.add_user(user, grupo)
    return "User has been correctly added to Group"

@app.route("/new_user", methods=["POST"])
def insert_user():
    name = request.form.get("character_name")
    pos.create_user(name)
    return "User has been correctly created"


app.run()