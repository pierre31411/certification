import streamlit as st
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

# --- Chargement du modèle et du préprocesseur
model = load_model("model_ann_leakyrelu.keras")
preprocessor = joblib.load("preprocessor.pkl")

# --- Interface utilisateur
surface_m2 = st.slider("Surface (m²)", min_value=10, max_value=900, value=80)
statut = st.selectbox("Statut du logement", ["Locataire", "Propriétaire"])
patrimoine_estime = st.number_input("Patrimoine estimé (€)", min_value=0, value=50000)
montant_couvert = st.number_input("Montant couvert (€)", min_value=0, value=150000)

# --- Création du DataFrame brut utilisateur
input_dict = {
    "surface_m2": [surface_m2],
    "statut_logement": [statut],
    "patrimoine_estime": [patrimoine_estime],
    "montant_couvert": [montant_couvert]
}
df_input = pd.DataFrame(input_dict)

# --- Application du même prétraitement qu’à l'entraînement
X_input_prep = preprocessor.transform(df_input)

# --- Prédiction
prediction = model.predict(X_input_prep)
prediction_value = round(prediction[0][0], 2)

# --- Affichage du résultat
st.subheader("Cotisation annuelle estimée :")
st.success(f"{prediction_value:.2f} €")
st.markdown("---")
# --- Affichage du résultat mensuel
cotisation_mensuelle = prediction_value / 12
st.subheader("Cotisation mensuelle estimée :")
st.info(f"{cotisation_mensuelle:.2f} € / mois")
