from apep_core.apep_input import ApepInput
from apep_core.apep_params import ApepParams

from sum_flow.sum_builder import SumBuilder

# EXECUTOR SIMULATION
if __name__ == "__main__":
   input_data = {"sumando_uno": 1, "sumando_dos": 2}

   apep_i = ApepInput(input_data)

   flow = SumBuilder.init_flow(apep_i, None)

   result = flow.execute()

   print(result.__dict__)
