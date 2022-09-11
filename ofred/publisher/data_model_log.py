from dataclasses import dataclass


@dataclass
class DataModelLog:
    req_index: str
    app: str
    req_body: str
    resp_body: str
    status_code: int
    reason: str

    server: str = ""
    browser: str = ""
    ip_req: str = ""
