import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib  # Se guardar el modelo

# Craga de datos
df = pd.read_csv("datos_procesados.csv")

print("Columnas disponibles en el dataset:", df.columns)

# Se asigna la variable objetivo
variable_objetivo = "dpnm"  

# Se definen las variables predictoras y la variable objetivo
X = df.drop(columns=["ID", variable_objetivo], errors="ignore")
y = df[variable_objetivo]

# Se divide en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Hacer las predicciones
y_pred = modelo.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)
print("Reporte de clasificación:\n", classification_report(y_test, y_pred))

# Guardar el modelo entrenado
joblib.dump(modelo, "modelo_entrenado.pkl")
print("Modelo guardado en 'modelo_entrenado.pkl'")