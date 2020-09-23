FROM python:3.8

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD ["./start.sh"]

