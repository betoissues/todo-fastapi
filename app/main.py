from fastapi import FastAPI
from . import models, db, routes, config

app = FastAPI()

db.Base.metadata.create_all(bind=db.engine)

api_v1 = FastAPI()
api_v1.include_router(
        routes.router,
        responses={404: {"description": "Not found"}},
        )


app.mount("/api/v1", api_v1)
