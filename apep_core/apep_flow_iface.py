from dataclasses import dataclass

from .apep_output import ApepOutput
from .apep_params import ApepParams

@dataclass
class ApepFlow:
    apep_params: ApepParams
    flow_input: object
    flow_name: str = None

    def __post_init__(self):
        self.flow_name = self.__class__.__name__

    def execute(self) -> ApepOutput:
        pass
    
    def callback(self) -> ApepOutput:
        pass