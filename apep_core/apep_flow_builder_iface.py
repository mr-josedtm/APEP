# from dataclasses import dataclass

from typing import Dict

from .apep_input import ApepInput
from .apep_params import ApepParams
from .apep_flow_iface import ApepFlow

from .apep_field_def import ApepFieldDef as fd
from .apep_field_type import ApepFieldType as ft

class ApepFlowBuilder:

    def get_input_contract() -> Dict:
        pass

    @classmethod
    def init_flow(sel, apep_input: ApepInput, params: ApepParams) -> ApepFlow:
    # Comprobar que las variables de entorno requeridas existen
    # Comprobar que los parámetros necesarios se han recibido
    # Comprobar que el input es válido y PARSEARLO AL OBJETO INTERNO

    # Devolver el flow que se va a lanzar y validado
        pass
