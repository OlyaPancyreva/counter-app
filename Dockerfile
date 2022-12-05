FROM python:3.8-alpine

RUN pip install --upgrade pip

WORKDIR /counter-app

COPY . /counter-app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["python", "app.py"]