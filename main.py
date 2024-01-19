from fastapi import FastAPI, Response, Query
from fastapi.responses import HTMLResponse
from module import generator, util
from typing import Optional

app = FastAPI()


@app.get("/")
def root():
    html_content = util.get_html_form()
    return HTMLResponse(content=html_content)


@app.get("/api")
def api(
    data: str = Query(min_length=1), 
    style: Optional[str] = "square", 
    bg_color: Optional[str] = None, 
    fill_color: Optional[str] = None
):
    return Response(generator.get_svg_string(data, style, bg_color, fill_color), media_type="image/svg+xml")
