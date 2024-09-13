FROM python:3.10-alpine AS builder

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
