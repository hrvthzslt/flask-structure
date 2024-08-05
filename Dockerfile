FROM python:3.10-slim

COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

WORKDIR /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
