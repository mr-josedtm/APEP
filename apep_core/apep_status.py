from enum import Enum

class ApepStatus(Enum):
    """ Enum to indicate the ApepFlow status """
    OK = 1
    KO = 2
    RUNNING = 3
    CALLBACK_EXC = 4
