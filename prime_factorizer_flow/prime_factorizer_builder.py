from typing import Dict

from apep_core.apep_flow_builder_iface import ApepFlowBuilder
from apep_core.apep_input import ApepInput
from apep_core.apep_params import ApepParams
from apep_core.apep_flow_iface import ApepFlow
from apep_core.apep_utils import input_to_dto
from apep_core.apep_field_def import ApepFieldDef as fd
from apep_core.apep_field_type import ApepFieldType as ft

from .prime_factorizer_flow import PrimeFactorizerFlow
from .prime_factorizer_dto import PrimeFactorizerDto

class PrimeFactorizerBuilder(ApepFlowBuilder):

    def get_input_contract() -> Dict:
        return {"number": (fd.REQUIRED, ft.INTEGER)}

    @classmethod
    def build_flow(cls, apep_input: ApepInput, params: ApepParams) -> ApepFlow:
        prime_factorizer_dto = input_to_dto(cls.get_input_contract(), apep_input, PrimeFactorizerDto())
        return PrimeFactorizerFlow(params, prime_factorizer_dto)