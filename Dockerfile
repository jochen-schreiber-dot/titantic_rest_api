FROM python:3.12.7
 
WORKDIR /app  
COPY requirements.txt .
COPY src/ /app/
COPY data/ /app/data

RUN pip install --no-cache-dir -r requirements.txt

ENV GUNICORN_CMD_ARGS="--bind 0.0.0.0:8002 -k uvicorn.workers.UvicornWorker"

EXPOSE 8002

CMD ["gunicorn" ,"main:app"]