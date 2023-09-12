from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from fastapi import UploadFile

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"])
templates = Jinja2Templates(directory="app/templates")
@router.get("app/templates/main_page", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})

