from .apep_data import ApepData
from dataclasses import dataclass
from typing import Callable


@dataclass
class ApepInput:
    """ Class to store input of a ApepFlow """
    input_data: ApepData
    mapper: Callable = None
    data: dict = None

    def __post_init__(self):
        if self.mapper:
            self.data = self.mapper(self.input_data.result)
        elif isinstance(self.input_data.result, dict):
            self.data = self.input_data.result
        else:
            # TODO Custo except
            raise Exception("Input data is not a dict and no mapper defined")

    def get_data_fields(self) -> object:
        """ Returns the existing fields """
        return list(self.data.keys())
    
    def get_field(self, field):
        return self.data.get(field)