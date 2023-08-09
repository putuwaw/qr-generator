# qr-generator

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)

QR Generator is a simple, free, and open source QR code generator for your `README` file. With this app, you can generate a QR code directly from your `README` file. This app is build using [python-qrcode](https://github.com/lincolnloop/python-qrcode) with [FastAPI](https://fastapi.tiangolo.com/) and deployed on [Vercel](https://vercel.com/).

## Features 💡

Using QR Generator, you can:

- [x] Generate QR code with custom data.
- [x] Costumize the QR code style, background color, and fill color.

## Usage 👨‍💻

Create your own QR code by modifying the `DATA` and `STYLE` in the URL below. You also can change the background color and fill color by changing the `BG_COLOR` and `FILL_COLOR` respectively. Curently there are 2 styles available: `square` and `circle`.

```url
https://qr-generator-putuwaw.vercel.app/api?data=<DATA>&style=<STYLE>bg_color=<BG_COLOR>&fill_color=<FILL_COLOR>
```

## Examples 🚀

Default style (transparent background and black fill color)

```
[![](https://qr-generator-putuwaw.vercel.app/api?data=https%3A%2F%2Fgithub.com%2Fputuwaw%2Fqr-generator&style=square)](https://qr-generator-putuwaw.vercel.app/api?data=https%3A%2F%2Fgithub.com%2Fputuwaw%2Fqr-generator&style=square)
```

[![](https://qr-generator-putuwaw.vercel.app/api?data=https%3A%2F%2Fgithub.com%2Fputuwaw%2Fqr-generator&style=square)](https://qr-generator-putuwaw.vercel.app/api?data=https%3A%2F%2Fgithub.com%2Fputuwaw%2Fqr-generator&style=square)

Circle shape with blue background and white fill color

```
[![](https://qr-generator-putuwaw.vercel.app/api?data=https%3A%2F%2Fgithub.com%2Fputuwaw%2Fqr-generator&style=circle&bg_color=blue&fill_color=white)](https://qr-generator-putuwaw.vercel.app/api?data=https%3A%2F%2Fgithub.com%2Fputuwaw%2Fqr-generator&style=circle&bg_color=blue&fill_color=white)
```

[![](https://qr-generator-putuwaw.vercel.app/api?data=https%3A%2F%2Fgithub.com%2Fputuwaw%2Fqr-generator&style=circle&bg_color=blue&fill_color=white)](https://qr-generator-putuwaw.vercel.app/api?data=https%3A%2F%2Fgithub.com%2Fputuwaw%2Fqr-generator&style=circle&bg_color=blue&fill_color=white)

> [!NOTE]  
> If you don't like to change the URL manually, you can use the [QR Generator](https://qr-generator-putuwaw.vercel.app/) web app.

## Prerequisites 📋

- Python 3.9 or higher
- Docker 24.0.4 or higher (optional)

## Installation 🛠

- Clone the repository:

```bash
git clone https://github.com/putuwaw/qr-generator.git
```

- Create a virtual environment and activate it:

```bash
python3.9 -m venv venv
source venv/bin/activate
```

- Install the dependencies:

```bash
make install
```

- Run the application:

```bash
make run
```

- You can also run the application using Docker:

```bash
docker pull putuwaw/qr-generator
```

- Run the application on port `8000`:

```bash
docker run -p 8000:8000 putuwaw/qr-generator
```

## Contributing 🤝

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
