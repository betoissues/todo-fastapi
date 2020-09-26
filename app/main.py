from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, db, routes, config

app = FastAPI()

db.Base.metadata.create_all(bind=db.engine)

api_v1 = FastAPI()
api_v1.include_router(
        routes.router,
        responses={404: {"description": "Not found"}},
        )

app.add_middleware(
        CORSMiddleware,
        allow_methods=["*"],
        allow_origins=["*"],
        allow_headers=["*"],
        allow_credentials=True
        )


app.mount("/api/v1", api_v1)
