from dataclasses import dataclass
from typing import Callable

@dataclass
class ApepInput:
    """ Class to store input of a ApepFlow """
    input_data: object
    mapper: Callable = None
    data: dict = None

    def __post_init__(self):
        if self.mapper:
            self.data = self.mapper(self.input_data)
        else:
            self.data = self.input_data

    def get_data_fields(self) -> object:
        """ Returns the existing fields """
        return list(self.data.keys())
    
    def get_field(self, field):
        return self.data.get(field)