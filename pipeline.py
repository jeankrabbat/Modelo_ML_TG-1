import os
import kaggle
import pandas as pd
import zipfile
import logging
from cryptography.fernet import Fernet
import json

# Configuración de logging
logging.basicConfig(filename="audit_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Cargar los roles del json
with open("config.json", "r") as f:
    roles = json.load(f)

# Generar la clave de cifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Función para verificar permiso
def check_access(role):
    '''Esta función sirve para verificar los permisos de los roles'''
    if role not in roles:
        logging.warning(f"Acceso denegado: Rol {role} no registrado")
        raise PermissionError("Acceso denegado: Rol no registrado")
    return roles[role]["access_level"]

# Cifrar datos sensibles
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(data):
    return cipher_suite.decrypt(encrypt_data.encode()).decode()

# Función para hacer backups
def backup_data(df, filename="backup_data.csv"):
    df.to_csv(filename, index=False)
    logging.info(f"Backup fue realizado con éxito en {filename}")

# Función principal de data pipeline
def main(role="admin"):
    try:
        # Verificar permiso
        access_level = check_access(role)
        if access_level == "restricted":
            logging.warning("Acceso restringido a este pipeline")
            raise PermissionError("No tienes permisos para ejecutar este pipeline")
        
        # Extracción de datos desde un archivo API de Kaggle
        kaggle.api.authenticate()

        dataset = 'mariosfish/default-of-credit-card-clients'

        kaggle.api.dataset_download_files(dataset, path='.', unzip=False)

        zip_file = f'{dataset.split("/")[-1]}.zip'

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall('.')
        
        os.remove(zip_file)

        df = pd.read_csv('default of credit card clients.csv')
        logging.info("Datos extraídos con éxito.")

        # Ejecutamos el backup
        backup_data(df)

        # Limpieza básica
        # df = df.drop_duplicates(inplace=True)
        # df = df.fillna(df.mean(), inplace=True)

        # Cifrar datos sensibles (en este caso ID de la persona, limit bal y edad)
        df["ID"] = df["ID"].astype(str).apply(encrypt_data)

        logging.info("Datos cifrados correctamente.")

        # Guardar los datos
        df.to_csv("datos_procesados.csv", index=False)
        logging.info("Datos procesados guardados en datos_procesados.csv")

        print("Pipeline ejecutado correctamente")
    
    except Exception as e:
        logging.error(f"Error en el pipeline: {e}")
        print(f"Error en el pipeline {e}")

if __name__ == "__main__":
    main("admin")