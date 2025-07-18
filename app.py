from flask import Flask, request, send_file, render_template
import cv2
import numpy as np
from sklearn.cluster import KMeans
import io

app = Flask(__name__)

STYLE_PRESETS = {
    'sketch':   {'line_size': 5,  'blur_value': 7,  'k': 20},  # Lightest lines, smoother transitions
    'soft':     {'line_size': 7,  'blur_value': 11, 'k': 16},  # Gentle edges and natural colors
    'classic':  {'line_size': 9,  'blur_value': 13, 'k': 12},  # Balanced and clear comic effect
    'bold':     {'line_size': 11, 'blur_value': 15, 'k': 8},   # Fewer colors, stronger outlines
    'ink':      {'line_size': 13, 'blur_value': 17, 'k': 5}    # Deep shadows, max stylization
}


def adjust_kernel_size(kernel_size):
    return kernel_size + 1 if kernel_size % 2 == 0 else kernel_size

def generate_edge_mask(img, line_size, blur_value):
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_blur = cv2.medianBlur(gray_img, blur_value)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, line_size, blur_value
    )
    return edges

def color_quantization(img, k):
    data = img.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k, random_state=42).fit(data)
    new_colors = kmeans.cluster_centers_[kmeans.labels_]
    return new_colors.reshape(img.shape).astype(np.uint8)

def generate_cartoon(img, edges):
    return cv2.bitwise_and(img, img, mask=edges)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_image():
    file = request.files['image']
    style = request.form.get('style', 'classic')
    if not file:
        return "No file uploaded", 400

    file_bytes = np.frombuffer(file.read(), np.uint8)
    img_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    if img_bgr is None:
        return "Invalid image", 400

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    preset = STYLE_PRESETS.get(style, STYLE_PRESETS['classic'])
    line_size = adjust_kernel_size(preset['line_size'])
    blur_value = adjust_kernel_size(preset['blur_value'])
    k = preset['k']

    edges = generate_edge_mask(img_rgb, line_size, blur_value)
    img_reduced = color_quantization(img_rgb, k)
    cartoon = generate_cartoon(img_reduced, edges)

    cartoon_bgr = cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR)
    _, buffer = cv2.imencode('.png', cartoon_bgr)
    return send_file(
        io.BytesIO(buffer),
        mimetype='image/png',
        as_attachment=False,
        download_name='comic.png'
    )

if __name__ == '__main__':
    app.run(debug=True)
