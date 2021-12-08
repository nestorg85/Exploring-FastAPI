from typing import List, Optional

from pydantic import BaseModel, validator

from database import db
from utils import validate_unique


class ClubMember(BaseModel):
    name: str
    age: int


class Club(BaseModel):
    id: Optional[str] = None
    club_members: List[ClubMember]
    club_name: str
    club_address: str


class ClubWrite(Club):
    @validator(*['club_name', 'club_address'])
    def unique_value(cls, value, values, field):
        if bool(list(filter(lambda x: validate_unique(field.name, x, value, values['id']), db.get_all()['clubs']))):
            raise ValueError('{} must be unique'.format(field.name))
        return value


class Clubs(BaseModel):
    clubs: List[Club]
