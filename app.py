import atexit
import datetime
import threading
import time

from dotenv import load_dotenv
from flask import Flask, request
from database.db import db
from database.dto.message.insert.insert import DTOInsertMessage
from database.dto.tag.insert.insert import DTOInsertTag
from database.dto.values import Status
from database.models.message import Message
from database.models.tag import Tag
from email_factory.email_factory import EmailFactory
from routing.documents.get.get_methods import document_get
from routing.documents.post.post_methods import document_post
from routing.files.get.get_methods import file_get
from routing.files.post.post_methods import file_post
from routing.messages.get.get_methods import message_get
from routing.messages.post.post_methods import message_post
from routing.messengers.get.get_methods import messenger_get
from routing.messengers.post.post_methods import messenger_post
from routing.profiles.get.get_methods import profile_get
from routing.profiles.post.post_methods import profile_post
from routing.profiles.put.put_methods import profile_put
from routing.tags.get.get_methods import tag_get
from routing.tags.post.post_methods import tag_post
from flask_socketio import SocketIO, join_room, disconnect, emit, send, leave_room, rooms

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(profile_get, url_prefix='/profiles-get')
app.register_blueprint(profile_post, url_prefix='/profiles-post')
app.register_blueprint(profile_put, url_prefix='/profiles-put')
app.register_blueprint(tag_get, url_prefix='/tags-get')
app.register_blueprint(tag_post, url_prefix='/tags-post')
app.register_blueprint(file_get, url_prefix='/files-get')
app.register_blueprint(file_post, url_prefix='/files-post')
app.register_blueprint(document_get, url_prefix='/documents-get')
app.register_blueprint(document_post, url_prefix='/documents-post')
app.register_blueprint(messenger_get, url_prefix='/messengers-get')
app.register_blueprint(messenger_post, url_prefix='/messengers-post')
app.register_blueprint(message_get, url_prefix='/messages-get')
app.register_blueprint(message_post, url_prefix='/messages-post')

db.init_app(app)
socketio = SocketIO(app)


@socketio.on('join_communication_room')
def handle_join_communication_room(data):
    room_id = data
    join_room(room_id)
    print(f"Пользователь добавлен в комнату {room_id}")
    emit('communication_room', {'text': 'Пользователь присоединился к комнате.'}, room=room_id)


@socketio.on('leave_communication_room')
def handle_leave_communication_room(data):
    room_id = data
    leave_room(room_id)
    emit('communication_room', {'text': 'Пользователь покинул комнату.'}, room=room_id)


@socketio.on('send_message')
def handle_send_message(data):
    model_message = Message.parse_raw(data)

    dto_message = DTOInsertMessage(db)
    result = dto_message.add_message(model_message)

    if result is not None:
        emit('message', result, room=model_message.messenger_id)


@app.route("/test_connection")
def test():
    return Status.OK.value



with app.app_context():
    db.create_all()
