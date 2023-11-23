from .sync_runner import sync_runner

# EXECUTOR SIMULATION
if __name__ == "__main__":
    ## EXECUTION INPUT ##
    # XXX it could be send in a rest request
    raw_start_data = {"sumando_uno": 10, "sumando_dos": 30}
    params_file = "C:/Users/Mx/workspace/APEP/apep_orchestrator/parameters_example.yml"
    sync_runner(raw_input_data=raw_start_data, params_path=params_file)
