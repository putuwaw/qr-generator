import qrcode
import io
from qrcode.image.svg import SvgPathImage
from qrcode.image.styles.moduledrawers.svg import SvgPathCircleDrawer
from qrcode.image.styles.moduledrawers.svg import SvgPathSquareDrawer
from PIL import Image, ImageDraw

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

def get_png_bytes(data: str, style: str, bg_color, fill_color, version=None, box_size=10, border=4) -> bytes:
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    # create image with circle style
    if style == "circle":
        img = qr.make_image(fill_color="white", back_color="white").convert('RGBA')
        circle_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(circle_img)

        for row in range(qr.modules_count):
            for col in range(qr.modules_count):
                if qr.modules[row][col]:
                    x0 = col * box_size + border * box_size
                    y0 = row * box_size + border * box_size
                    x1 = x0 + box_size
                    y1 = y0 + box_size
                    draw.ellipse([x0, y0, x1, y1], fill=fill_color)

        img = Image.alpha_composite(img, circle_img)
        if bg_color:
            background = Image.new('RGBA', img.size, bg_color)
            img = Image.alpha_composite(background, img)

        # convert image to bytes
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer.getvalue()

    else:
        img = qr.make_image(fill_color=fill_color, back_color=bg_color)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer.getvalue()