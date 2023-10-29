from dataclasses import dataclass

from apep_core.apep_flow_iface import ApepFlow
from apep_core.apep_output import ApepOutput
from apep_core.apep_metadata import ApepMetadata
from apep_core.apep_params import ApepParams

from .sum_dto import SumDto

@dataclass
class SumFlow (ApepFlow):
    flow_input: SumDto
    # Lo primero que haces es coger y mapear la entrada bien, validar, etc
    apep_params: ApepParams

    def execute(self) -> ApepOutput:
        exec_metadata = ApepMetadata(self.__class__.__name__)
        result = ApepOutput(exec_metadata)

        suma = self.flow_input.sumando_uno + self.flow_input.sumando_dos

        result.add_result(suma)

        result.set_execution_end()
    
        return result
            
    # Quizas mejor
    def callback(self) -> ApepOutput:
        # quizás mejor aquí el tratamiento del callback
        pass

    # Control function to show the behaviour of drilling the params through steps
    def _print_params(self):
        params = self.apep_params.params
        print(f"Printing execution params at class: {self.__class__}")
        for key, value in params.items():
            print(f"{key}: {value}")