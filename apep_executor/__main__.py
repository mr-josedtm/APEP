from apep_core.apep_input import ApepInput
from apep_core.apep_params import ApepParams

from sum_flow.sum_builder import SumBuilder

# EXECUTOR SIMULATION
if __name__ == "__main__":

   params = {"my_parameter": "first parameter value", "other_param": 1.0}
   apep_params = ApepParams(params)



   input_data = {"sumando_uno": 1, "sumando_dos": 2}
   apep_i = ApepInput(input_data)
   sum_flow = SumBuilder.init_flow(apep_i, apep_params)
   sum_flow_result = sum_flow.execute()
   print(sum_flow_result.__dict__)
