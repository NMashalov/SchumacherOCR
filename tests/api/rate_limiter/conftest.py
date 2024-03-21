import pytest
import fastapi

@pytest.fixture(name='fastapi_app')
def fastapi_app(**limiter_args):
    app = fastapi.FastAPI()
    # mock_handler = mock.Mock()
    # mock_handler.level = logging.INFO
    # limiter.logger.addHandler(mock_handler)
    return app