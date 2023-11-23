import logging as log
import yaml
from apep_core.apep_params import ApepParams

def read_params(params_file_path):
    params = {}
    if params_file_path is not None:
        try:
            with open(params_file_path, 'r', encoding='utf-8') as file:
                loaded_params = yaml.safe_load(file)
                if loaded_params is not None:
                    params = loaded_params
        except FileNotFoundError:
            log.error("El archivo %s no fue encontrado", params_file_path)
        except Exception as e:
            log.error("Error al leer el archivo %s: %s", params_file_path, e)
    
    return ApepParams(params)
