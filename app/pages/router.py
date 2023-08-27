from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]

)

'''templates = Jinja2Templates(directory="app/templates")

@router.get("/hotels")
async def get_hotels_page(
    request:Request
):
    return templates.TemplateResponse(name="hotels.html", context={"request":request})
'''

templates = Jinja2Templates(directory="app/templates")


@router.get("/main_page/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("main_page.html", {"request": request, "id": id})
