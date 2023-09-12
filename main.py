from fastapi import FastAPI
from fastapi import FastAPI, Request

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.pages.router import router as router_pages

app = FastAPI()
app.mount("/main_page", StaticFiles(directory="app/templates/images/main_page"), name="main_page")
app.include_router(router_pages)








