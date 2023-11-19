from dataclasses import dataclass, field
from typing import List
from .apep_metadata import ApepMetadata
from .apep_status import ApepStatus
from .apep_data import ApepData

@dataclass
class ApepOutput:
    """ Class to store output of an ApepFlow execution
        TODO: Más enfocado a la salida de una ejecución 
    """
    metadata: ApepMetadata
    success_result: List[ApepData] = field(default_factory=list)
    error_result: str = None

    def add_result(self, result: ApepData) -> None:
        self.success_result.append(result)

    def set_error(self, error_info: str) -> None:
        self.error_result = error_info

    def set_execution_end(self, status: ApepStatus = ApepStatus.OK, message: str = "Execution ended") -> None:
        self.metadata.set_execution_end(status, len(self.success_result), message)

    def get_results(self):
        return self.success_result
