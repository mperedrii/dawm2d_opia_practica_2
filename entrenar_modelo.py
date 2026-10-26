"""Entrena el modelo de precios de casas en California y lo guarda en modelo_california.pkl.

Autores: Mykola Peredrii, Andres Cordoba
"""

import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

MODEL_PATH = "modelo_california.pkl"

# X es un DataFrame: el modelo guarda los nombres de las columnas (MedInc, HouseAge...)
X, y = fetch_california_housing(as_frame=True, return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=12,
    min_samples_leaf=5,
    n_jobs=-1,
    random_state=42,
)
model.fit(X_train, y_train)

print(f"R2 en test: {r2_score(y_test, model.predict(X_test)):.3f}")
joblib.dump(model, MODEL_PATH, compress=3)
print(f"Modelo guardado en {MODEL_PATH}")
