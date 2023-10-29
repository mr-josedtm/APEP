from enum import Enum

class ApepFieldDef(Enum):
    """ Enum to indicate the ApepInput data definition
        REQUIRED: the field must be present and not null
        NULLABLE: the field must be present and could be null
        OPTIONAL: the field could be present and could be null
    """
    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"
    NULLABLE = "NULLABLE"
