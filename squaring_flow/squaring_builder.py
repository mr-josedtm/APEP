from typing import Dict

from apep_core.apep_flow_builder_iface import ApepFlowBuilder
from apep_core.apep_input import ApepInput
from apep_core.apep_params import ApepParams
from apep_core.apep_flow_iface import ApepFlow
from apep_core.apep_utils import input_to_dto
from apep_core.apep_field_def import ApepFieldDef as fd
from apep_core.apep_field_type import ApepFieldType as ft

from .squaring_flow import SquaringFlow
from .squaring_dto import SquaringDto

class SquaringBuilder(ApepFlowBuilder):

    def get_input_contract() -> Dict:
        return {"base": (fd.REQUIRED, ft.INTEGER)}

    @classmethod
    # Refactor class methods
    def build_flow(cls, apep_input: ApepInput, params: ApepParams) -> ApepFlow:
        squaring_dto = input_to_dto(cls.get_input_contract(), apep_input, SquaringDto())
        return SquaringFlow(params, squaring_dto)