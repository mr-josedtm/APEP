from dataclasses import dataclass

@dataclass
class ApepInput:
    """ Class to store input of a ApepFlow """
    data: dict

    def get_data_fields(self) -> object:
        """ Returns the existing fields """
        return list(self.data.keys())
    
    def get_field(self, field):
        return self.data.get(field)