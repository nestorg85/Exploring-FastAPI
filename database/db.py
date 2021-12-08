import json
import os
import uuid
from typing import Union

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_all() -> dict:
    with open(os.path.join(dir_path, 'data.json')) as file:
        return json.load(file)


def create_club(club: dict) -> dict:
    clubs: dict = get_all()
    club['id'] = uuid.uuid4().hex
    clubs['clubs'].append(club)

    with open(os.path.join(dir_path, 'data.json'), 'w') as file:
        json.dump(clubs, file, indent=4, sort_keys=False)

    return club


def update_club(club_id: str, club: dict) -> Union[dict, None]:
    clubs = get_all()
    try:
        current_club = next(filter(lambda x: x['id'] == club_id, clubs['clubs']))
    except StopIteration:
        raise None
    else:
        current_club.update(club)
        with open(os.path.join(dir_path, 'data.json'), 'w') as file:
            json.dump(clubs, file, indent=4, sort_keys=False)
        return current_club
