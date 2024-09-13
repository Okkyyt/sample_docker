FROM python:3.9-slim
RUN pip install fastapi uvicorn
#　main.pyを/appにコピー
COPY main.py /app/main.py
#　/appに移動
WORKDIR /app
#　main.pyを実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
