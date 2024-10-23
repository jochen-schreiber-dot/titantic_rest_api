curl http://127.0.0.1:8000/alives
curl http://127.0.0.1:8000/alives/1
curl http://127.0.0.1:8000/classes
curl http://127.0.0.1:8000/classes/1
curl http://127.0.0.1:8000/decks
curl http://127.0.0.1:8000/decks/1
curl http://127.0.0.1:8000/embarktowns
curl http://127.0.0.1:8000/embarktowns/1
curl http://127.0.0.1:8000/embarked
curl http://127.0.0.1:8000/embarked/1
curl http://127.0.0.1:8000/sex
curl http://127.0.0.1:8000/sex/1
curl http://127.0.0.1:8000/who
curl http://127.0.0.1:8000/who/1
curl http://127.0.0.1:8000/observations
curl -d '{"survived":0,"pclass":3,"age":29.0,"sibsp":1,"parch":0,"fare":7.25,"adult_male":true,"alone":false,"sex_id":0,"embarked_id":2,"class_id":1,"who_id":2,"deck_id":-1,"embark_town_id":2,"alive_id":0}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/observations