from apep_core.apep_input import ApepInput
from apep_core.apep_params import ApepParams
from apep_core.apep_output import ApepOutput

from sum_flow.sum_builder import SumBuilder
from squaring_flow.squaring_builder import SquaringBuilder

# EXECUTOR SIMULATION
if __name__ == "__main__":

   params = {"my_parameter": "first parameter value", "other_param": 1.0}
   apep_params = ApepParams(params)

   flow_start_data = {"sumando_uno": 1, "sumando_dos": 2}

   sum_apep_i = ApepInput(flow_start_data)
   sum_flow = SumBuilder.init_flow(sum_apep_i, apep_params)
   sum_flow_result: ApepOutput  = sum_flow.execute()
   print("SumFlow Result:")
   print(sum_flow_result.__dict__)
   print(sum_flow_result.get_results())


   for result in sum_flow_result.get_results():
      # XXX El tema de que si los campos de salida del anterior no tienen nada que ver con este, peta
      # Recordar que el builder informa del contrato, intentar aprovecharlo
      # sum_result_to_squaring_input_contract

      squaring_apep_i = ApepInput(result)
      squaring_flow = SquaringBuilder.init_flow(sum_apep_i, apep_params)
      squaring_flow_result = squaring_flow.execute()
      print("SquaringFlow Result:")
      print(squaring_flow_result.__dict__)

   
