from uvicorn import run
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from .routers import users
from .routers import mangas

app = FastAPI()
router = APIRouter(prefix='/api')

router.include_router(users.router)
router.include_router(mangas.router)

app.include_router(router)

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)
