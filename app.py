from datetime import datetime

from flask import Flask, request, render_template
import os
import socket

import init_db

app = Flask(__name__)


# localhost:port/ (возвращается текущее значение счётчика, инкремента не происходит);
@app.route('/')
def start():
    html = "<h3>Значение счетчика: {counter}</h3>"
    return html.format(counter=init_db.get_counter())


# localhost:port/stat (возвращается текущее значение счётчика, и происходит инкремент);
@app.route('/stat')
def stat():
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    client_info = request.headers.get('User-Agent')

    init_db.set_counter(dt, client_info)

    html = "<h3 style='color:red'>Вы увеличили значение!</h3>" \
           "<h3>Значение счетчика: {counter}</h3>"
    return html.format(counter=init_db.get_counter())


# localhost:port/users (возвращает таблицу со всеми данными)
@app.route('/users')
def get_users():
    return render_template('index.html', users=init_db.get_table())


# localhost:port/about функция hello в gist только с вашим именем <h3> Hello , _your_name_</h3>.
@app.route('/hello')
def hello():
    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
