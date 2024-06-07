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
                        <label for="formate" class="form-label">Format</label>
                        <select class="form-select" name="formate" id="formate" onchange="togglePngOptions()">
                            <option selected value="svg">SVG</option>
                            <option value="png">PNG</option>
                        </select>
                    </div>
                    <div id="png-options" style="display: none;">
                        <div class="mb-3">
                            <label for="version" class="form-label">Version</label>
                            <select class="form-select" name="version" id="version">
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                                <option value="6">6</option>
                                <option value="7">7</option>
                                <option value="8">8</option>
                                <option value="9">9</option>
                                <option value="10">10</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="box_size" class="form-label">Box Size: <span id="box_size_value">10</span></label>
                            <input type="range" class="form-range" id="box_size" name="box_size" min="1" max="100" value="10" oninput="updateBoxSizeValue(this.value)">
                            <div class="d-flex justify-content-between">
                                <span>1</span>
                                <span>50</span>
                                <span>100</span>
                            </div>
                        </div>
                        <div class="mb-3">
                            <label for="border" class="form-label">Border Size: <span id="border_value">4</span></label>
                            <input type="range" class="form-range" id="border" name="border" min="0" max="50" value="4" oninput="updateBorderSizeValue(this.value)">
                            <div class="d-flex justify-content-between">
                                <span>1</span>
                                <span>4</span>
                                <span>50</span>
                            </div>
                        </div>
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
            <script>
                function togglePngOptions() {
                    var formatSelect = document.getElementById("formate");
                    var pngOptions = document.getElementById("png-options");
                    if (formatSelect.value === "png") {
                        pngOptions.style.display = "block";
                    } else {
                        pngOptions.style.display = "none";
                    }
                }
                function updateBoxSizeValue(value) {
                    document.getElementById("box_size_value").innerText = value;
                }
                function updateBorderSizeValue(value) {
                    document.getElementById("border_value").innerText = value;
                }
            </script>
        </body>
        </html>
    """
