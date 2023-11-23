from uvicorn import run
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from .routers import users

app = FastAPI()
router = APIRouter(prefix='/api')

router.include_router(users.router)

app.include_router(router)

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)
