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

    def check_required_envs() -> None:
        pass

    @classmethod
    def build_flow(sel, apep_input: ApepInput, params: ApepParams) -> ApepFlow:
        pass
