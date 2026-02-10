import cv2
import numpy as np

# Prétraitement des images
def preprocess(uploaded_file):
    # Lire l'image depuis l'upload
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    # Redimensionner pour simplifier
    image = cv2.resize(image, (256, 256))
    # Normaliser entre 0 et 1
    return image / 255.0

# Calcul simple NDVI
def compute_ndvi(image):
    red = image[:, :, 2]
    nir = image[:, :, 1]  # simplification pour hackathon
    ndvi = (nir - red) / (nir + red + 1e-6)
    return ndvi
