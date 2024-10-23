# Titanic REST API example
- Running locally on port 8002
- Data from https://www.google.com/url?q=https://github.com/davidjamesknight/SQLite_databases_for_learning_data_science&source=gmail&ust=1729765290120000&usg=AOvVaw1-7KQX90VF3hGobf8-Rrgw

## Setup

### Docker build & run
1. docker build . -t=titanticapp
2. docker run -it -p 8002:8002 titanticapp    

### Local execution
1. cd src
2. gunicorn main:app -b 0.0.0.0:8002 -w 4 -k uvicorn.workers.UvicornWorker

### Python venv
1. python3 -m venv venv
2. source venv/bin/activate
3. python3 -m pip install -r requirements.txt

## Example calls
- curl http://127.0.0.1:8002/alives
- curl http://127.0.0.1:8002/alives/1
- curl http://127.0.0.1:8002/classes
- curl http://127.0.0.1:8002/classes/1
- curl http://127.0.0.1:8002/decks
- curl http://127.0.0.1:8002/decks/1
- curl http://127.0.0.1:8002/embarktowns
- curl http://127.0.0.1:8002/embarktowns/1
- curl http://127.0.0.1:8002/embarked
- curl http://127.0.0.1:8002/embarked/1
- curl http://127.0.0.1:8002/sex
- curl http://127.0.0.1:8002/sex/1
- curl http://127.0.0.1:8002/who
- curl http://127.0.0.1:8002/who/1
- curl http://127.0.0.1:8002/observations
- curl -d '{"survived":0,"pclass":3,"age":29.0,"sibsp":1,"parch":0,"fare":7.25,"adult_male":true,"alone":false,"sex_id":0,"embarked_id":2,"class_id":1,"who_id":2,"deck_id":-1,"embark_town_id":2,"alive_id":0}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8002/observations