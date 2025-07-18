# 🎨 Comic Book Effect Generator

## Project Overview

The Comic Book Effect Generator is a web application that transforms ordinary images into stylized comic book art. Users can upload an image and apply various pre-defined comic book effects, each with distinct line styles, color palettes, and overall aesthetics. The application processes images on the backend using Python and provides the transformed image back to the user for preview and download.

## Features

* **Image Upload:** Easily upload your images (JPG, PNG, etc.) via a user-friendly interface.
* **Multiple Comic Styles:** Choose from 5 distinct comic book style presets:
    * **Sketch Tint:** For a soft, light pencil drawing look.
    * **Soft Comic:** Produces smooth edges and natural-looking colors.
    * **Classic Comic:** Offers a balanced and clear traditional comic effect (default).
    * **Bold Comic:** Delivers a more pronounced, pop-art inspired style with stronger outlines.
    * **Ink Explosion:** Generates dramatic, inky outlines and deep shadows for maximum stylization.
* **Real-time Processing:** Images are processed on the server and displayed dynamically.
* **Image Download:** Download the generated comic image directly from the browser.
* **Responsive Design:** A simple, clean, and modern web interface.

## Technical Stack

* **Backend Framework:** Flask (Python)
* **Image Processing:** OpenCV (`cv2`) for edge detection, blurring, and image manipulation.
* **Color Quantization:** Scikit-learn (`KMeans`) for reducing the number of colors in the image, giving it a flat, comic-book feel.
* **Frontend:** HTML, CSS, JavaScript
    * **HTML:** For structuring the web page.
    * **CSS:** For styling (including custom fonts from Google Fonts).
    * **JavaScript:** For handling image uploads, style selection, and dynamic display of results using `fetch` API.
* **Language:** Python

## How to Run Locally

Follow these steps to set up and run the Comic Book Effect Generator on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/vivek955-hub/Comic-Effect-Generator.git](https://github.com/vivek955-hub/Comic-Effect-Generator.git)
    cd Comic-Effect-Generator
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install Flask opencv-python scikit-learn numpy
    ```

5.  **Run the Flask Application:**
    ```bash
    python app.py
    ```

6.  **Access the Application:**
    Open your web browser and navigate to:
    ```
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```

## Project Structure