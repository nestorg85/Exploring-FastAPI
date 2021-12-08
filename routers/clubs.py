import fastapi
from fastapi import HTTPException

from database import db
from models.clubs import Club, Clubs, ClubWrite

router = fastapi.APIRouter()


@router.get('/api/clubs/', response_model=Clubs, tags=["clubs"], status_code=200)
def read_clubs():
    return db.get_all()


@router.post('/api/clubs/', response_model=Club, tags=["clubs"], status_code=201)
def create_club(club: ClubWrite):
    return db.create_club(club.dict())


@router.patch('/api/clubs/{club_id}/', response_model=Club, tags=["clubs"], status_code=200)
def update_club(club_id: str, club: ClubWrite):
    if not club_id == club.id:
        raise HTTPException(status_code=400, detail=[
            {
                "loc": [
                    "body",
                    "id"
                ],
                "msg": "field value not match with url",
                "type": "value_error.no_match"
            }
        ])
    club = db.update_club(club_id, club.dict())
    if club is None:
        raise HTTPException(status_code=404, detail="Club not found")

    return club
