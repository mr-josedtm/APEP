from apep_core.apep_input import ApepInput
from apep_core.apep_params import ApepParams
from apep_core.apep_output import ApepOutput

from sum_flow.sum_builder import SumBuilder
from squaring_flow.squaring_builder import SquaringBuilder

from .mappers.sum_to_squaring_mapper import sum_result_to_squaring_input_contract

# EXECUTOR SIMULATION
if __name__ == "__main__":

   params = {"my_parameter": "first parameter value", "other_param": 1.0}
   apep_params = ApepParams(params)

   flow_start_data = {"sumando_uno": 1, "sumando_dos": 2}

   sum_apep_i = ApepInput(flow_start_data)
   sum_flow = SumBuilder.build_flow(sum_apep_i, apep_params)
   sum_flow_result: ApepOutput  = sum_flow.execute()
   print("SumFlow Result:")
   print(sum_flow_result.__dict__)
   print(sum_flow_result.get_results())

   print("Saving metadata: ", sum_flow_result.metadata)

   for result in sum_flow_result.get_results():

      # FIXME si no hay mapper, hace falta el __dict__ y no debería ser necesario
      # porque el mapper ya devuelve un dict
      # squaring_apep_i = ApepInput(result.__dict__)
      squaring_apep_i = ApepInput(result, sum_result_to_squaring_input_contract)
      squaring_flow = SquaringBuilder.build_flow(squaring_apep_i, apep_params)
      squaring_flow_result = squaring_flow.execute()
      print("Saving metadata: ", squaring_flow_result.metadata)
      print("SquaringFlow Result:")
      print(squaring_flow_result.__dict__)
