from flask import Flask
import os
import socket

app = Flask(__name__)
counter = 0


# функция для увеличения значения счетчика
def set_counter():
    global counter
    counter += 1
    return counter


# localhost:port/ (возвращается текущее значение счётчика, инкремента не происходит);
@app.route('/')
def start():
    html = "<h3>Значение счетчика: {counter}</h3>"
    return html.format(counter=counter)


# localhost:port/stat (возвращается текущее значение счётчика, и происходит инкремент);
@app.route('/stat')
def stat():
    html = "<h3 style='color:red'>Вы увеличили значение!</h3>" \
           "<h3>Значение счетчика: {counter}</h3>"
    return html.format(counter=set_counter())


# localhost:port/about функция hello в gist только с вашим именем <h3> Hello , _your_name_</h3>.
@app.route('/hello')
def hello():
    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
