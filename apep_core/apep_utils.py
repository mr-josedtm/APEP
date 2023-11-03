from typing import Dict, List, Tuple
from .apep_field_def import ApepFieldDef as fd
from .apep_input import ApepInput

def _check_required_fields(input_contract: Dict, data_fields: List) -> None:
    if not input_contract or not data_fields:
        # TODO
        raise Exception("Not input contract or data fields provided")

    # Keep in mind that nullable fields must be present but it's value could be None
    required_keys = [key for key, (required, _) in input_contract.items() if required == fd.REQUIRED or required == fd.NULLABLE]

    # Check if all required fields are present
    # Data could have more elements that the required ones (optional data or useless data for this flow)
    check_required_keys = all(element in data_fields for element in required_keys)

    if not check_required_keys:
        # TODO create exception
        raise Exception("Not all required fields found")
    

# Coge el ApepInput, lo valida y devuelve el objeto que espera el flow
def _data_parser(required_field: str, required_validations: Tuple, apep_input: ApepInput ) -> any:

    definition_type = required_validations[0]
    value_type = required_validations[1]

    # Take care about the behaviour of .get_field() function
    # if the required field doesn't exist, it's gonna return a None value
    attr_value = apep_input.get_field(required_field)
    
    if isinstance(attr_value, value_type.value)\
        or (definition_type == fd.OPTIONAL and attr_value is None):
        return attr_value
    else:
        #TODO more descriptive exception
        raise Exception(f"Not matching type for {required_field}")
    
def input_to_dto(input_contract: Dict, apep_input: ApepInput, dto: object) -> object:

        _check_required_fields(input_contract, apep_input.get_data_fields())

        for required_field, required_validations in input_contract.items():            
            value = _data_parser(required_field, required_validations, apep_input)
            setattr(dto, required_field, value)

        return dto