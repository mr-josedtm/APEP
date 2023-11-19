# TODO
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    # # Inicia las ejecuciones en paralelo
    # futures = {executor.submit(context.call_activity, 'append_sufix', res): res for res in count_result}

    # # Espera la finalización de todas las ejecuciones en paralelo
    # for future in concurrent.futures.as_completed(futures):
    #     try:
    #         resultado = future.result()
    #         sufix_results.append(resultado)
    #     except Exception as e:
    #         print(f"ERROR!! {e}")