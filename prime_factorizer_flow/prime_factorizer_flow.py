from dataclasses import dataclass

from apep_core.apep_flow_iface import ApepFlow
from apep_core.apep_output import ApepOutput
from apep_core.apep_data import ApepData
from apep_core.apep_metadata import ApepMetadata
from apep_core.apep_params import ApepParams

from .prime_factorizer_dto import PrimeFactorizerDto
from .prime_factorizer_result import PrimeFactorizerResult

@dataclass
class PrimeFactorizerFlow (ApepFlow):
    flow_input: PrimeFactorizerDto
    # Lo primero que haces es coger y mapear la entrada bien, validar, etc
    apep_params: ApepParams
    flow_name: str = None

    def __post_init__(self):
        self.flow_name = self.__class__.__name__


    def _to_primes(self, number: int):
        prime_factors = []
        divider = 2

        while number > 1:
            while number % divider == 0:
                prime_factors.append(divider)
                number //= divider
            divider += 1

        return prime_factors

    def execute(self) -> ApepOutput:
        self._print_params()

        exec_metadata = ApepMetadata(self.flow_name)
        result = ApepOutput(exec_metadata)

        factors = self._to_primes(self.flow_input.number)

        for factor in factors:
            data = ApepData(PrimeFactorizerResult(factor), 0)
            result.add_result(data)

        result.set_execution_end()
    
        return result
            
    # Quizas mejor
    def callback(self) -> ApepOutput:
        # quizás mejor aquí el tratamiento del callback
        pass

    # Control function to show the behaviour of drilling the params through steps
    def _print_params(self):
        params = self.apep_params.params
        print(f">>> Printing execution params at class: {self.flow_name}")
        for key, value in params.items():
            print(f"{key}: {value}")