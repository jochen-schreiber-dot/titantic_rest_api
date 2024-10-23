from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()

class Alive(Base):
    __tablename__ = 'alive'
    
    alive_id = Column(Integer, primary_key=True, index=True)
    alive = Column(String)

class AliveModel(BaseModel):
    alive_id: int
    alive: str | None

class Class(Base):
    __tablename__ = 'class'
    
    class_id = Column(Integer, primary_key=True, index=True)
    class_text = Column("class", String)

class ClassModel(BaseModel):
    class_id: int
    class_text: str | None

class Deck(Base):
    __tablename__ = 'deck'
    
    deck_id = Column(Integer, primary_key=True, index=True)
    deck = Column(String)

class DeckModel(BaseModel):
    deck_id: int
    deck: str | None

class EmbarkTown(Base):
    __tablename__ = 'embarktown'
    
    embark_town_id = Column(Integer, primary_key=True, index=True)
    embark_town = Column(String)

class EmbarkTownModel(BaseModel):
    embark_town_id: int
    embark_town: str | None

class Embarked(Base):
    __tablename__ = 'embarked'
    
    embarked_id = Column(Integer, primary_key=True, index=True)
    embarked = Column(String)

class EmbarkedModel(BaseModel):
    embarked_id: int
    embarked: str | None

class Observation(Base):
    __tablename__ = 'observation'
    __mapper_args__ = {
        'primary_key': ("survived","pclass", "age","sibsp", "fare", "parch", "adult_male", "alone", "sex_id", "embarked_id", "class_id", "who_id", "deck_id", "embark_town_id", "alive_id"),
    }
    survived = Column(Integer)
    pclass   = Column(Integer)
    age      = Column(Float)
    sibsp    = Column(Integer)
    parch    = Column(Integer)
    fare     = Column(Float)
    adult_male = Column(Boolean)
    alone = Column(Boolean)
    sex_id = Column(Integer)
    embarked_id = Column(Integer)
    class_id = Column(Integer)
    who_id = Column(Integer)
    deck_id = Column(Integer)
    embark_town_id = Column(Integer)
    alive_id = Column(Integer)

class ObservationModel(BaseModel):

    survived : int
    pclass   : int
    age      : float | None
    sibsp    : int
    parch    : int
    fare     : float
    adult_male : bool
    alone : bool
    sex_id : int
    embarked_id : int
    class_id : int
    who_id : int
    deck_id : int
    embark_town_id : int
    alive_id : int

class Sex(Base):
    __tablename__ = 'sex'
    
    sex_id = Column(Integer, primary_key=True, index=True)
    sex = Column(String)

class SexModel(BaseModel):
    sex_id: int
    sex: str | None

class Who(Base):
    __tablename__ = 'who'
    
    who_id = Column(Integer, primary_key=True, index=True)
    who = Column(String)

class WhoModel(BaseModel):
    who_id: int
    who: str | None