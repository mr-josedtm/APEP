# from dataclasses import dataclass

from typing import Dict

from .apep_input import ApepInput
from .apep_params import ApepParams
from .apep_flow_iface import ApepFlow

# TODO create as interface

class ApepFlowBuilder:

    def get_input_contract(self) -> Dict:
        pass

    def check_required_envs(self) -> None:
        pass

    @classmethod
    def build_flow(sel, apep_input: ApepInput, params: ApepParams) -> ApepFlow:
        pass
