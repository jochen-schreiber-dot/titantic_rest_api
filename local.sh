cd src
gunicorn main:app -b 0.0.0.0:8002 -w 4 -k uvicorn.workers.UvicornWorker --reload
