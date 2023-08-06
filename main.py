from fastapi import FastAPI, Response, Query
from fastapi.responses import HTMLResponse
from module import generator, util

app = FastAPI()


@app.get("/")
def root():
    html_content = util.get_html_form()
    return HTMLResponse(content=html_content)


@app.get("/api")
def api(data: str = Query(min_length=1), style: str = "square", bg_color = None, fill_color = None):
    return Response(generator.get_svg_string(data, style, bg_color, fill_color), media_type="image/svg+xml")
