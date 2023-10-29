from sum_flow.sum_result import SumResult


def sum_result_to_squaring_input_contract(sum_result: SumResult):
    # Validate types
    return {"base": sum_result.valor_sumado}
