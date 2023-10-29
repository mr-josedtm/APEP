from dataclasses import dataclass

from apep_core.apep_flow_iface import ApepFlow
from apep_core.apep_output import ApepOutput
from apep_core.apep_metadata import ApepMetadata
from apep_core.apep_params import ApepParams

from .sum_dto import SumDto
from .sum_result import SumResult

@dataclass
class SumFlow (ApepFlow):
    flow_input: SumDto
    # Lo primero que haces es coger y mapear la entrada bien, validar, etc
    apep_params: ApepParams
    flow_name: str = None

    def __post_init__(self):
        self.flow_name = self.__class__.__name__

    def execute(self) -> ApepOutput:
        self._print_params()

        exec_metadata = ApepMetadata(self.flow_name)
        result = ApepOutput(exec_metadata)

        suma = self.flow_input.sumando_uno + self.flow_input.sumando_dos

        result.add_result(SumResult(suma))

        result.set_execution_end()
    
        return result
            
    # Quizas mejor
    def callback(self) -> ApepOutput:
        # quizás mejor aquí el tratamiento del callback
        pass

    # Control function to show the behaviour of drilling the params through steps
    def _print_params(self):
        params = self.apep_params.params
        print(f"Printing execution params at class: {self.flow_name}")
        for key, value in params.items():
            print(f"{key}: {value}")