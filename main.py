import fastapi
import uvicorn

from routers import clubs

api = fastapi.FastAPI()


def configure():
    api.include_router(clubs.router)


configure()
if __name__ == '__main__':
    uvicorn.run(api)
