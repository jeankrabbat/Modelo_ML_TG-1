# Proyecto: Predicción de Incumplimiento de Pago con IA

## Descripción

Este proyecto tiene como objetivo desarrollar un sistema que permita predecir el incumplimiento de pago en clientes de tarjetas de crédito mediante un Data Pipeline y un modelo de Inteligencia Artificial (IA). La solución se implementa en dos partes principales:

- **Data Pipeline:** Extrae y procesa el dataset de Kaggle, aplicando técnicas de respaldo, cifrado y transformación para asegurar la calidad y seguridad de los datos.
- **Modelo de IA e Integración:** Se entrena un modelo para predecir el incumplimiento de pago y se integra en una aplicación web interactiva (Streamlit) que permite hacer predicciones en tiempo real o por lotes.

## Contenido del Repositorio

- **pipeline.py:**  
  Implementa el Data Pipeline, incluyendo la extracción del dataset desde Kaggle, el procesamiento y la transformación de los datos (por ejemplo, el cifrado de información sensible) y la generación de un archivo procesado.

- **app.py:**  
  Aplicación web desarrollada en Streamlit que carga el modelo de IA entrenado (almacenado en `modelo_entrenado.pkl`), permite ingresar datos manualmente o subir un CSV para realizar predicciones masivas, y muestra los resultados.

- **config.json:**  
  Archivo de configuración que define los roles y permisos necesarios para ejecutar el pipeline. Ejemplo:

  ```json
  {
      "admin": {"access_level": "full"},
      "user": {"access_level": "restricted"}
  }

- **modelo_entrenado.pkl:**
  Archivo que contiene el modelo de IA entrenado. Es necesario tener este archivo en la raíz para que la aplicación funcione correctamente.

- **requirements.txt:**
  Lista de dependencias y librerías necesarias para ejecutar el proyecto.

 - **DOCUMENTACION_TECNICA.md:**
  Documento que explica en detalle la arquitectura del Data Pipeline, la integración del modelo de IA y las decisiones de diseño en cuanto a seguridad, criptografía y limpieza de datos.


## Instrucciones de Ejecución

 - **Requisitos del Sistema:**
   Python: 3.7 o superior.
   
 - **Librerías:**
 Las dependencias se listan en requirements.txt. Para instalarlas, ejecuta:
  pip install -r requirements.txt

## Ejecución del Data Pipeline

1 - Asegúrate de que el archivo config.json esté correctamente configurado según los roles y permisos.

2- Ejecuta el pipeline: python pipeline.py
- **El script se autentica con la API de Kaggle y descarga el dataset default-of-credit-card-clients.**
- **Descomprime el archivo ZIP descargado, realiza un respaldo del dataset original y lo guarda como backup_data.csv.**
- **Aplica la transformación de datos, entre ellas el cifrado de información sensible, y genera el archivo datos_procesados.csv.**
- **Se registran todas las acciones en audit_log.txt para mantener un registro de auditoría.**


## Ejecución de la Aplicación en Streamlit

1-Verifica que modelo_entrenado.pkl se encuentre en la raíz del repositorio.

2-Inicia la aplicación de Streamlit: streamlit run app.py (Se debe de ingresar en la terminal Visual Studio Code)

- **La aplicación permite ingresar datos manualmente o cargar un archivo CSV para realizar predicciones en lote.**
- **Se muestran en pantalla tanto la predicción individual como la masiva, junto con las probabilidades asociadas, y se ofrece la opción de descargar los resultados en CSV.**

   
















