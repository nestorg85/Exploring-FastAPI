import fastapi
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from routers import clubs

api = fastapi.FastAPI()

origins = [
    "http://localhost:4200",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def configure():
    api.include_router(clubs.router)


configure()
if __name__ == '__main__':
    uvicorn.run(api)
