# Python Fast API Test

This project is a personal initial testing for the [FastAPI](https://fastapi.tiangolo.com/) framework. The code expose
three methods of an API to create, update and read information from a local [JSON file](database/data.json) database.

## API endpoints

The exposed methods are described below.

### Read Clubs

This is a GET method exposed at [/api/clubs/](http://localhost:8080/api/clubs/). This method return the whole of clubs
registered into the database.

### Create Club

This is a POST method exposed at [/api/clubs/](http://localhost:8080/api/clubs/). This method allows to add a new club
record into the database.

### Update Club

This is a PATCH method exposed at [/api/clubs/{club_id}/](http://localhost:8080/api/clubs/). This method allows to
update an existing record into the database.

*More details [here](http://localhost:8000/docs). Is required to run the server first.*

## Prerequisites

Is required to install some libraries before run the server.

Run in the console:

```shell
pip install -r requirements.txt 
```

## Run a local server

The project is configured to run with [Uvicorn](https://www.uvicorn.org/).

Run in the console:

```shell
python main.py
```






