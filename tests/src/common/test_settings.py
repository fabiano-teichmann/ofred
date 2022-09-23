import os

import pytest
from pydantic import ValidationError

from settings import Settings


class TestSettings:
    @pytest.fixture
    def fixture_settings(self):
        os.environ["SECRET_KEY"] = "SECRET"
        os.environ["USER_POSTGRES"] = "SECRET"
        os.environ["HOST_POSTGRES"] = "SECRET"
        os.environ["DB_POSTGRES"] = "SECRET"
        os.environ["PASSW_POSTGRES"] = "SECRET"
        os.environ["USER_RABBIT"] = "SECRET"
        os.environ["HOST_RABBIT"] = "SECRET"
        os.environ["PASSW_RABBIT"] = "SECRET"

    def test_should_raise_exception_when_not_defined_variables(self):
        with pytest.raises(ValidationError):
            Settings()

    def test_should_return_object_when_variables_is_defined(self, fixture_settings):
        assert Settings().secret_key == "SECRET"
