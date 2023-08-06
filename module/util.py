def get_html_form():
    return """
        <!DOCTYPE html>
        <html lang="en" data-bs-theme="dark">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>QR Code Generator</title>
            <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9"
            crossorigin="anonymous"
            />
        </head>
        <style>
            main {
            max-width: 400px;
            }
        </style>
        <body>
            <main class="m-auto p-3">
                <form action="/api" method="get">
                    <div class="mb-3">
                        <label for="data" class="form-label">Text</label>
                        <input
                            type="text"
                            class="form-control"
                            id="data"
                            name="data"
                            placeholder="Enter QR code text or link here..."
                            required
                        />
                    </div>
                    <div class="mb-3">
                        <label for="style" class="form-label">Style</label>
                        <select class="form-select" name="style" id="style">
                            <option selected value="square">Square</option>
                            <option value="circle">Circle</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="bg-color" class="form-label">Background Color</label>
                        <input 
                            class="form-control" 
                            id="bg-color"
                            name="bg_color" 
                            type="color" 
                            value="#ffffff">
                    </div>
                    <div class="mb-3">
                        <label for="fill-color" class="form-label">Fill Color</label>
                        <input
                            class="form-control" 
                            id="fill-color"
                            name="fill_color" 
                            type="color" 
                        />
                    </div>
                    <button type="submit" value="submit" class="btn btn-primary w-100">
                        Generate
                    </button>
                </form>
            </main>
            <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm"
            crossorigin="anonymous"
            ></script>
        </body>
        </html>
    """
