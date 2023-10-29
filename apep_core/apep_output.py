from dataclasses import dataclass, field
from typing import List
from .apep_metadata import ApepMetadata
from .apep_status import ApepStatus

@dataclass
class ApepOutput:
    """ Class to store output of an ApepFlow execution """
    metadata: ApepMetadata
    success_result: List[object] = field(default_factory=list)
    error_result: str = None

    def add_result(self, result) -> None:
        self.success_result.append(result)

    def set_error(self, error) -> None:
        self.error_result = error

    def set_execution_end(self, status: ApepStatus = ApepStatus.OK, message: str = "Execution ended") -> None:
        self.metadata.set_execution_end(status, message)
