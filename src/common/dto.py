from datetime import datetime
from pydantic import BaseModel, root_validator


class DTOLog(BaseModel):
    app: str
    domain: str
    req_index: str = ""
    event_name: str = ""
    req_path: str = ""
    req_body: str
    resp_body: str
    status_code: int
    dt_current_timestamp: datetime
    metadata: dict = {}
    log_level: str = "INFO"

    @root_validator(pre=True)
    def generate_req_index(cls, values):
        req_index = values['event_name'] if values.get('event_name') else values.get('req_path')
        if not req_index:
            raise ValueError('both fields event_name, req_path cannot be empty')
        if values.get('req_index') is None:
            values["req_index"] = req_index

        return values
