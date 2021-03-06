# fastapi import
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

# database import
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# routes from spotify api
from .api import spotify

tags_metadata = [
    {
        "name": "spotify",
        "description": "Operations with Spotify API integration. The **login** logic is also here.",
        "externalDocs": {
            "description": "spotify external docs",
            "url": "https://developer.spotify.com/documentation/"
        },
    }
]

app = FastAPI(    
    title = "My Spotify API",
    description = "This is my API Spotify integration",
    version = "0.1",
    openapi_tags = tags_metadata
)

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API ROUTES
app.include_router(spotify.router, tags=["spotify"])


# testing fast api
@app.post("/hello_world")
def hello_world():
    """
    hello world! post.
    """
    return {
        "message": "hello world!"
    }