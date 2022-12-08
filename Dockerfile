FROM python:3.8-alpine

RUN pip install --upgrade pip

WORKDIR /counter-app

COPY . /counter-app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
COPY . .

CMD ["python", "app.py"]