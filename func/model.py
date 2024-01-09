import joblib
import numpy as np

# Chargement du modèle sauvegardé
model_filename = './static/data/linear_regression_model.joblib'
loaded_model = joblib.load(model_filename)

def predict(form):
    """Effectue une prédiction sur les données du formulaire"""
    input_data = np.array([[form.year_of_construction.data, form.surface_area.data, form.num_observations.data]])
    prediction = loaded_model.predict(input_data)
    return round(prediction[0], 1)
