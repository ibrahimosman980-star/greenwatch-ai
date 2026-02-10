import numpy as np

# Prédiction simple basée sur la différence NDVI
def predict(ndvi_before, ndvi_after, threshold=0.2):
    diff = ndvi_before - ndvi_after
    mask = diff > threshold  # True = zone dégradée
    return mask
