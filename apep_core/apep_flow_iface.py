from dataclasses import dataclass

from .apep_output import ApepOutput
from .apep_params import ApepParams

class ApepFlow:
    apep_params: ApepParams
    flow_input: object

    def execute(self) -> ApepOutput:
        pass
    
    def callback(self) -> ApepOutput:
        pass