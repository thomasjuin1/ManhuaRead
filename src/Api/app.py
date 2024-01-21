from uvicorn import run
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from .routers import users
from .routers import mangas
from .routers import manga_users

app = FastAPI()
router = APIRouter(prefix='/api')

router.include_router(users.router)
router.include_router(mangas.router)
router.include_router(manga_users.router)

app.include_router(router)

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)
