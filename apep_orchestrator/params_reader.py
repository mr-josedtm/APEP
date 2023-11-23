import logging as log
import yaml
from apep_core.apep_params import ApepParams

def read_params(params_file_path):
    try:
        with open(params_file_path, 'r', encoding='utf-8') as file:
            loaded_params = yaml.safe_load(file)
            params = loaded_params or {}
        return ApepParams(params)
    except FileNotFoundError:
        log.error("El archivo %s no fue encontrado", params_file_path)
    except Exception as e:
        log.error("Error al leer el archivo %s: %s", params_file_path, e)
