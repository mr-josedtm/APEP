from typing import List
from dataclasses import dataclass, field

@dataclass
class ApepParams:
    """ Class to store params of an ApepPipeline used by one or several ApepFlow"""
    # Idealmente serían inmutables
    params: dict = field(default_factory=dict)

    def get_configured_params(self) -> List[str]:
        """ Returns a list of configured params """
        return list(self.params.keys())
