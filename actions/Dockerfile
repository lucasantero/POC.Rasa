FROM rasa/rasa-sdk:1.7.0

USER root

WORKDIR /app

COPY requirements.txt /app

COPY . /app/actions

RUN pip3 install -r requirements.txt

#CMD ["start", "--actions", "actions"]

user 1001