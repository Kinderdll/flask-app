
FROM python:3.8-slim

# Set environment variables for disk size logs and peformance 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=main.py

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc \
    && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
#COPY instance /app/instance
#COPY migrations /app/migrations
#Migrations
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

EXPOSE 5000

CMD ["python", "main.py"]


