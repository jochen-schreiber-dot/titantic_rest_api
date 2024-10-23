FROM python:3.12.7
 
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV GUNICORN_CMD_ARGS="-b 0.0.0.0:8002 -w 4 -k uvicorn.workers.UvicornWorker"
EXPOSE 8002

WORKDIR /app/src
CMD ["gunicorn" ,"main:app"]