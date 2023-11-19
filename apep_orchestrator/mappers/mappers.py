from sum_flow.sum_result import SumResult
from prime_factorizer_flow.prime_factorizer_result import  PrimeFactorizerResult


def sum_result_to_prime_fact_input_contract(sum_result: SumResult):
    # Validate types
    return {"number": sum_result.valor_sumado}



def prime_fact_result_to_squaring_input_contract(prime_fact_result: PrimeFactorizerResult):
    # Validate types
    return {"base": prime_fact_result.factor_found}

