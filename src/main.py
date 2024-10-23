from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from typing import List
from lib.classes import *
from lib.database import get_db
from loguru import logger

import sqlite3
import pandas as pd

app = FastAPI()
logger.add("../titanic_api.log", rotation="12:00")

@app.get("/")
def get_root_message():
    logger.success("root endpoint hit")
    return {"message": "Hello World"}

####################
#
# ALIVES ENDPOINTS
#
####################
@app.get("/alives", response_model=List[AliveModel])
def get_alives(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.success("alives endpoint hit")
    alives = db.query(Alive).offset(skip).limit(limit).all()
    return alives

@app.get("/alives/{alive_id}", response_model=AliveModel)
def get_alive(alive_id: int, db: Session = Depends(get_db)):
    logger.success("alives endpoint hit with id " + alive_id)
    alive = db.query(Alive).filter(Alive.alive_id == alive_id).first()
    if alive is None:
        raise HTTPException(status_code=404, detail="Alive not found")
    return alive

####################
#
# CLASS ENDPOINTS
#
####################
@app.get("/classes", response_model=List[ClassModel])
def get_classes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.success("classes endpoint hit")
    class_obj = db.query(Class).offset(skip).limit(limit).all()
    return class_obj

@app.get("/classes/{class_id}", response_model=ClassModel)
def get_class(class_id: int, db: Session = Depends(get_db)):
    logger.success("classes endpoint hit with id " + class_id)
    class_obj = db.query(Class).filter(Class.class_id == class_id).first()
    if class_obj is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return class_obj


####################
#
# DECK ENDPOINTS
#
####################
@app.get("/decks", response_model=List[DeckModel])
def get_decks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.success("decks endpoint hit")
    decks = db.query(Deck).offset(skip).limit(limit).all()
    return decks

@app.get("/decks/{deck_id}", response_model=DeckModel)
def get_deck(deck_id: int, db: Session = Depends(get_db)):
    logger.success("decks endpoint hit with id " + deck_id)
    deck = db.query(Deck).filter(Deck.deck_id == deck_id).first()
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    return deck


####################
#
# EMBARKTOWN ENDPOINTS
#
####################
@app.get("/embarktowns", response_model=List[EmbarkTownModel])
def get_embark_towns(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.success("embarktowns endpoint hit")
    decks = db.query(EmbarkTown).offset(skip).limit(limit).all()
    return decks

@app.get("/embarktowns/{embark_town_id}", response_model=EmbarkTownModel)
def get_embark_town(embark_town_id: int, db: Session = Depends(get_db)):
    logger.success("embarktowns endpoint hit with id " + embark_town_id)
    embark_town = db.query(EmbarkTown).filter(EmbarkTown.embark_town_id == embark_town_id).first()
    if embark_town is None:
        raise HTTPException(status_code=404, detail="EmbarkTown not found")
    return embark_town


####################
#
# EMBARKED ENDPOINTS
#
####################
@app.get("/embarked", response_model=List[EmbarkedModel])
def get_embarked_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.success("embarked endpoint hit")
    embarked = db.query(Embarked).offset(skip).limit(limit).all()
    return embarked

@app.get("/embarked/{embarked_id}", response_model=EmbarkedModel)
def get_embarked(embarked_id: int, db: Session = Depends(get_db)):
    logger.success("embarked endpoint hit with id " + embarked_id)
    embarked = db.query(Embarked).filter(Embarked.embarked_id == embarked_id).first()
    if embarked is None:
        raise HTTPException(status_code=404, detail="Embarked not found")
    return embarked


####################
#
# OBSERVATION ENDPOINTS
#
####################

@app.get("/obs", response_model=List[ObservationModel])
def get_obs():
    conn = sqlite3.connect('../data/titanic.db')
    cursor = conn.cursor()
    df = pd.read_sql_query("SELECT * FROM observation", conn)
    logger.success("obs endpoint hit")
    logger.success(len(df))
    json_data = df.to_json(orient='records')
    return JSONResponse(content=json_data)

@app.get("/observations", response_model=List[ObservationModel])
def get_observations(skip: int = 0, limit: int = 2000, db: Session = Depends(get_db)):
    logger.success("observations endpoint hit")
    logger.success(len(db.query(Observation).all()))
    return db.query(Observation).all()
    #return observations

@app.post("/observations", response_model=ObservationModel)
def create_observation(observation: ObservationModel, db: Session = Depends(get_db)):
    logger.success("observations endpoint hit with post")
    try:
        observation_obj = Observation(**observation.dict())
        db.add(observation_obj)
        db.commit()
        db.refresh(observation_obj)
        return observation_obj
    except Exception as e:
       return {"message": "Error {}".format(e)}
    finally:
        db.close()

####################
#
# SEX ENDPOINTS
#
####################
@app.get("/sex", response_model=List[SexModel])
def get_sex_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.success("sex endpoint hit")
    sex = db.query(Sex).offset(skip).limit(limit).all()
    return sex

@app.get("/sex/{sex_id}", response_model=SexModel)
def get_sex(sex_id: int, db: Session = Depends(get_db)):
    logger.success("sex endpoint hit with id " + sex_id)
    sex = db.query(Sex).filter(Sex.sex_id == sex_id).first()
    if sex is None:
        raise HTTPException(status_code=404, detail="Sex not found")
    return sex

####################
#
# WHO ENDPOINTS
#
####################
@app.get("/who", response_model=List[WhoModel])
def get_who_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.success("who endpoint hit")
    who = db.query(Who).offset(skip).limit(limit).all()
    return who

@app.get("/who/{who_id}", response_model=WhoModel)
def get_who(who_id: int, db: Session = Depends(get_db)):
    logger.success("who endpoint hit with id " + who_id)
    who = db.query(Who).filter(Who.who_id == who_id).first()
    if who is None:
        raise HTTPException(status_code=404, detail="Who not found")
    return who