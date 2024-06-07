from fastapi import FastAPI, Response, Query
from fastapi.responses import HTMLResponse, StreamingResponse
from module import generator, util
from typing import Optional
import io

app = FastAPI()


@app.get("/")
def root():
    html_content = util.get_html_form()
    return HTMLResponse(content=html_content)


@app.get("/api")
def api(
    data: str = Query(min_length=1), 
    style: Optional[str] = "square", 
    formate: Optional[str] = "svg",
    version: Optional[int] = None,
    box_size: Optional[int] = None,
    border: Optional[int] = None,
    bg_color: Optional[str] = None, 
    fill_color: Optional[str] = None
):
    if formate == "png":
        image_bytes = generator.get_png_bytes(data, style, bg_color, fill_color, version, box_size, border)
        buffer = io.BytesIO(image_bytes)
        return StreamingResponse(buffer, media_type="image/png")
    else:
        return Response(generator.get_svg_string(data, style, bg_color, fill_color), media_type="image/svg+xml")
