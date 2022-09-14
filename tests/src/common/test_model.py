from datetime import datetime

import pytest
from pydantic import ValidationError

from common.model import DataModelLog


class TestModel:
    @pytest.fixture
    def fixture_base_payload(self) -> dict:
        return {"app": "Test", "req_event": "test_event",
                "req_body": "{'a': 1}", "resp_body": "{'msg': 'Hello'}", "status_code": 200,
                "dt_current_timestamp": datetime.now(),
                "metadata": {"app": "test", "ip": "127.0.0.1"}}

    @pytest.mark.parametrize("field", ["app", "req_event", "req_body", "resp_body",
                                       "status_code", "dt_current_timestamp"])
    def test_should_handle_exception_when_payload_not_has_fields_required(self, field, fixture_base_payload):
        del fixture_base_payload[field]
        with pytest.raises(ValidationError):
            DataModelLog(**fixture_base_payload)

    def test_should_return_data_model_with_req_index_with_test_event(self, fixture_base_payload):
        assert DataModelLog(**fixture_base_payload).req_index == fixture_base_payload["req_event"]

    def test_should_return_data_model_with_req_index_with_req_index(self, fixture_base_payload):
        fixture_base_payload["req_index"] = "req_index"
        assert DataModelLog(**fixture_base_payload).req_index == "req_index"
