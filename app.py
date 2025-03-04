import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Cargar el modelo entrenado
modelo = joblib.load("modelo_entrenado.pkl")

# Definir las columnas de entrada (ajustar según tu dataset)
columnas_modelo = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE',
                   'PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6',
                   'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
                   'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']

# Función para realizar predicción
def predecir_pago(data):
    df = pd.DataFrame([data], columns=columnas_modelo)
    prediccion = modelo.predict(df)[0]
    probabilidad = modelo.predict_proba(df)[0][1]  # Probabilidad de default
    return prediccion, probabilidad

# Interfaz en Streamlit
st.title("Predicción de Incumplimiento de Pago con IA")
st.write("Ingrese los datos del cliente para predecir si incumplirá el pago.")

# Valores de prueba predefinidos
valores_prueba = [50000, 1, 2, 1, 30, 0, 0, 0, 0, 0, 0,
                  20000, 18000, 17000, 16000, 15000, 14000,
                  1000, 1500, 2000, 2500, 3000, 3500]

# Crear entradas para los datos del usuario con valores predefinidos
entrada = []
for i, col in enumerate(columnas_modelo):
    valor = st.number_input(f"{col}", value=valores_prueba[i])
    entrada.append(valor)

# Botón para hacer la predicción manualmente
if st.button("Predecir"):
    prediccion, probabilidad = predecir_pago(entrada)
    resultado = "✅ No incumplirá el pago" if prediccion == 0 else "⚠ Incumplirá el pago"
    
    st.subheader("Resultado de la Predicción:")
    st.write(resultado)
    st.write(f"Probabilidad de incumplimiento: {probabilidad:.2%}")

# Hacer una predicción automática al abrir la app
st.subheader("Predicción Automática:")
prediccion_auto, probabilidad_auto = predecir_pago(valores_prueba)
resultado_auto = "✅ No incumplirá el pago" if prediccion_auto == 0 else "⚠ Incumplirá el pago"
st.write(resultado_auto)
st.write(f"Probabilidad de incumplimiento: {probabilidad_auto:.2%}")

# Permitir cargar un archivo CSV para predicciones masivas
st.subheader("Cargar archivo CSV para predicciones masivas")
archivo = st.file_uploader("Sube un archivo CSV con los datos", type=["csv"])

if archivo is not None:
    df_cargado = pd.read_csv(archivo)
    
    # Asegurar que las columnas coinciden con las del modelo
    df_cargado = df_cargado[columnas_modelo]  

    # Hacer predicciones
    predicciones = modelo.predict(df_cargado)
    probabilidades = modelo.predict_proba(df_cargado)[:, 1]  # Probabilidad de default

    # Agregar resultados al DataFrame
    df_cargado["Predicción"] = predicciones
    df_cargado["Probabilidad"] = probabilidades

    # Mostrar los resultados en la app
    st.write("Resultados de las predicciones:")
    st.write(df_cargado)

    # Botón para descargar los resultados corregido
    csv = df_cargado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Descargar resultados",
        data=csv,
        file_name="predicciones.csv",
        mime="text/csv"
    )
