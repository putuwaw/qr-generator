import qrcode
from qrcode.image.svg import SvgPathImage
from qrcode.image.styles.moduledrawers.svg import SvgPathCircleDrawer
from qrcode.image.styles.moduledrawers.svg import SvgPathSquareDrawer


def get_svg_string(data: str, style: str, bg_color, fill_color) -> str:
    # create drawer either square or circle
    drawer = SvgPathCircleDrawer() if style == "circle" else SvgPathSquareDrawer()

    qr = qrcode.QRCode(image_factory=SvgPathImage)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(module_drawer=drawer)
    result = img.to_string()
    result = str(result)

    # add background color
    if bg_color is not None:
        if len(bg_color) == 0:
            bg_color = "rgba(0, 0, 255, 0)"
        idx = result.find("<path")
        rect = f'<rect width="100%" height="100%" fill="{bg_color}" />'
        result = result[:idx] + rect + result[idx:]

    # add fill color
    if fill_color is not None:
        if len(fill_color) == 0:
            fill_color = 'fill="#000000"'
        result = result.replace('fill="#000000"', f'fill="{fill_color}"')

    return result[2:-1]
