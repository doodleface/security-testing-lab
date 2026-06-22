FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

EXPOSE 9443

CMD ["hypercorn", "app:app", "--bind", "0.0.0.0:9443", "--certfile", "/certs/server.crt", "--keyfile", "/certs/server.key"]
