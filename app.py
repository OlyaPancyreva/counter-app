from datetime import datetime

from flask import Flask, request, render_template
import os
import socket
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


# создаем элементы таблицы
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(80), nullable=False)
    client_info = db.Column(db.String(200), nullable=False)

    def __init__(self, datetime, client_info):
        self.datetime = datetime
        self.client_info = client_info


db.create_all()


def get_items():
    return db.session.query(Item).all()


def set_item(dt, client_info):
    db.session.add(Item(dt, client_info))
    db.session.commit()


# localhost:port/ (возвращается текущее значение счётчика, инкремента не происходит);
@app.route('/', methods=['GET'])
def start():
    html = "<h3>Значение счетчика: {counter}</h3>"
    return html.format(counter=get_items())


# localhost:port/stat (возвращается текущее значение счётчика, и происходит инкремент);
@app.route('/stat', methods=['POST'])
def stat():
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    client_info = request.headers.get('User-Agent')

    set_item(dt, client_info)

    html = "<h3 style='color:red'>Вы увеличили значение!</h3>" \
           "<h3>Значение счетчика: {counter}</h3>"
    return html.format(counter=get_items())


# localhost:port/about функция hello в gist только с вашим именем <h3> Hello , _your_name_</h3>.
@app.route('/hello')
def hello():
    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())
