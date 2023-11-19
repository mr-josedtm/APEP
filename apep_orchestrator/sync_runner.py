from apep_core.apep_input import ApepInput
from apep_core.apep_params import ApepParams
from apep_core.apep_data import ApepData
from apep_core.apep_data_buffer import ApepDataBuffer
from apep_core.apep_flow_builder_iface import ApepFlowBuilder
from typing import Callable

from apep_logger.apep_log import save_to_mongo

from sum_flow.sum_builder import SumBuilder
from squaring_flow.squaring_builder import SquaringBuilder
from prime_factorizer_flow.prime_factorizer_builder import PrimeFactorizerBuilder

from .mappers.mappers import prime_fact_result_to_squaring_input_contract, sum_result_to_prime_fact_input_contract


def executor(flow_builder: ApepFlowBuilder, params: ApepParams, data_buffer: ApepDataBuffer, mapper: Callable = None) -> ApepDataBuffer:

    step_result = ApepDataBuffer()

    # TODO ejecuciones priorizadas. O devolver ordenadas o controlar el orden (mejor esto para asincronas)
    # 1 obtener prioridades disponibles
    # 2 ejecutar todos los prioridad menor
    # 3 seguir ejecutando prioridades posteriores
    for result in data_buffer.get_piorized_data():
        apep_input = ApepInput(result, mapper)
        current_flow = flow_builder.build_flow(apep_input, params)
        current_flow_result = current_flow.execute()

        step_result.add_results(current_flow_result.get_results())
        
        save_to_mongo(current_flow_result)

        ###### ONLY FOR PoC ######
        print(f"=== Pinting results for {current_flow_result.metadata.execution_id}: ")
        for res in current_flow_result.get_results():
            print(res.__dict__)

    return step_result

def sync_runner():
    raw_params = {"my_parameter": "first parameter value", "other_param": 1.0}
    apep_params = ApepParams(raw_params)

    ## EXECUTION INPUT ##
    raw_start_data = {"sumando_uno": 10, "sumando_dos": 30}
    start_data = ApepData(raw_start_data, 0)
    flow_start_data = ApepDataBuffer([start_data])

    # Step 0
    sum_flow_result = executor(SumBuilder, apep_params, flow_start_data)
    
    # Step 1
    prime_fact_flow_result = executor(PrimeFactorizerBuilder, apep_params, sum_flow_result, sum_result_to_prime_fact_input_contract)

    # Step 2
    squaring_flow_result = executor(SquaringBuilder, apep_params, prime_fact_flow_result, prime_fact_result_to_squaring_input_contract)
