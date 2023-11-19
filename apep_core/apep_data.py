from dataclasses import dataclass

@dataclass
class ApepData:
    """
        TODO
    """

    result: object = None
    priority: int = None

    def set_data(self, result: object, priority: int = 0):
        self.result = result
        self.priority = priority
