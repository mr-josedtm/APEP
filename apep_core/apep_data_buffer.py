from dataclasses import dataclass, field
from typing import List, Set
from .apep_data import ApepData

@dataclass
class ApepDataBuffer:
    """
    TODO
    """
    data: List[ApepData] = field(default_factory=list)

    def add_result(self, result: ApepData):
        self.data.append(result)
    
    def add_results(self, results: List[ApepData]):
        self.data.extend(results)

    def get_available_priorities(self) -> Set[int]:
        # TODO
        return None

    def get_piorized_data(self) -> List[ApepData]:
        return self.data
