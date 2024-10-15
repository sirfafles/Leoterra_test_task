FROM python:3.9-slim

RUN pip install --no-cache-dir flask flask-cors PyJWT

WORKDIR /flask_app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "app.py"]

EXPOSE 5000
