FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY protocol_lab.proto ./
COPY server.py ./
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protocol_lab.proto

EXPOSE 50051 50052

CMD ["python", "server.py"]
