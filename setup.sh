python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt

gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
#uvicorn app:app --host 0.0.0.0 --port 8000 --reload

docker build . -t=titanticapp && docker run -it -p 8002:8002 titanticapp    