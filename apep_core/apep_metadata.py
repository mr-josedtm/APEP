from dataclasses import dataclass, field
from datetime import datetime
from .apep_status import ApepStatus

@dataclass
class ApepMetadata:
    """ Class to store metadata of an ApepFlow execution """
    flow_class_name: str
    execution_id: str = None
    # TODO set correct type an meassure strategy
    execution_init_time: datetime = datetime.now()
    execution_end_time: datetime = None
    execution_time: datetime = None
    status: ApepStatus = ApepStatus.RUNNING
    message: str = None
    # Free field to store any information about the flow and persist it in the database
    metadata_result: dict = field(default_factory=dict)

    def __post_init__(self):
        self.execution_id = f"{self.flow_class_name}_{self.execution_init_time.strftime('%Y%m%d%H%M%S%f')}"

    def set_execution_end(self, status: ApepStatus, message: str = "Execution ended"):
        self.status = status
        self. execution_end_time = datetime.now()
        self.execution_time = self.execution_end_time - self.execution_init_time
        self.message = message
