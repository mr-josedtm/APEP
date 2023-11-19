from dataclasses import dataclass, field
from datetime import datetime, timedelta
from .apep_status import ApepStatus

@dataclass
class ApepMetadata:
    """ Class to store metadata of an ApepFlow execution """
    flow_class_name: str
    execution_id: str = None
    execution_init_time: datetime = datetime.now()
    execution_end_time: datetime = None
    execution_time: timedelta = None

    status: ApepStatus = ApepStatus.RUNNING
    message: str = None

    total_results: int = 0

    # Free field to store any information about the flow and persist it in the database
    metadata_result: dict = field(default_factory=dict)

    def __post_init__(self):
        self.execution_id = f"{self.flow_class_name}_{self.execution_init_time.strftime('%Y%m%d%H%M%S%f')}"

    def set_execution_end(self, status: ApepStatus, total_results: int, message: str = "Execution ended"):
        self.status = status
        self. execution_end_time = datetime.now()
        self.execution_time = self.execution_end_time - self.execution_init_time
        self.message = message
        self.total_results = total_results
    
    def get_metadata_doc(self):
        metadata_doc = {
            'flow_class_name': self.flow_class_name,
            'execution_id': self.execution_id,
            'execution_init_time': self.execution_init_time,
            'execution_end_time': self.execution_end_time,
            'execution_time': self.execution_time.total_seconds(),
            'status': self.status.value,
            'total_results': self.total_results,
            'message': self.message,
            'metadata_result': self.metadata_result,
        }
        return metadata_doc
