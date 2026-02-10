import streamlit as st
import numpy as np
from utils import preprocess, compute_ndvi
from model import predict

st.set_page_config(page_title="GreenWatch AI", layout="wide")
st.title("🌍 GreenWatch AI")
st.write("Détection de la déforestation et de la désertification")

# Upload des images
col1, col2 = st.columns(2)
with col1:
    img_before = st.file_uploader("Image AVANT", type=["png", "jpg"])
with col2:
    img_after = st.file_uploader("Image APRÈS", type=["png", "jpg"])

# Bouton pour analyser
if st.button("🔍 Analyser"):
    if img_before and img_after:
        # Prétraitement
        image_b = preprocess(img_before)
        image_a = preprocess(img_after)

        # Calcul NDVI
        ndvi_b = compute_ndvi(image_b)
        ndvi_a = compute_ndvi(image_a)

        # Détection de dégradation
        mask = predict(ndvi_b, ndvi_a)

        # Taux de dégradation
        rate = np.sum(mask) / mask.size * 100
        st.success(f"Taux de dégradation : {rate:.2f}%")

        # Affichage des zones dégradées
        st.image(mask.astype(int)*255, caption="Zones dégradées (rouge)")
    else:
        st.warning("Veuillez charger les deux images")
