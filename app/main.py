from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.config import PSQL_ENVIRONMENT
from app.database import models
<<<<<<< HEAD
from app.database.database import engine
from app.dependencies import (
    MEDIA_PATH, STATIC_PATH, templates)
from app.routers import agenda, dayview, event, profile, email, invitation
=======
from app.database.database import engine, get_db
from app.dependencies import (logger, MEDIA_PATH, STATIC_PATH, templates)
from app.internal import daily_quotes, json_data_loader
from app.routers import (
    agenda, calendar, categories, dayview, email,
    event, invitation, profile, search, telegram, whatsapp
)
from app.telegram.bot import telegram_bot
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10


def create_tables(engine, psql_environment):
    if 'sqlite' in str(engine.url) and psql_environment:
        raise models.PSQLEnvironmentError(
            "You're trying to use PSQL features on SQLite env.\n"
            "Please set app.config.PSQL_ENVIRONMENT to False "
            "and run the app again."
        )
    else:
        models.Base.metadata.create_all(bind=engine)


create_tables(engine, PSQL_ENVIRONMENT)
app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")
app.mount("/media", StaticFiles(directory=MEDIA_PATH), name="media")

<<<<<<< HEAD
app.include_router(profile.router)
app.include_router(event.router)
app.include_router(agenda.router)
app.include_router(dayview.router)
app.include_router(email.router)
app.include_router(invitation.router)
=======
json_data_loader.load_to_db(next(get_db()))

app.logger = logger

routers_to_include = [
    agenda.router,
    calendar.router,
    categories.router,
    dayview.router,
    email.router,
    event.router,
    invitation.router,
    profile.router,
    search.router,
    telegram.router,
    whatsapp.router,
]
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10

for router in routers_to_include:
    app.include_router(router)

telegram_bot.set_webhook()


# TODO: I add the quote day to the home page
# until the relevant calendar view will be developed.
@app.get("/")
@logger.catch()
async def home(request: Request, db: Session = Depends(get_db)):
    quote = daily_quotes.quote_per_day(db)
    return templates.TemplateResponse("home.html", {
        "request": request,
        "message": "Hello, World!",
<<<<<<< HEAD
=======
        "quote": quote
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10
    })
