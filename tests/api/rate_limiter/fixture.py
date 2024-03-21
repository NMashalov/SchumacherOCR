import fastapi
from starlette.testclient import TestClient
import pytest

@pytest.fixture
def set_limiter(fastapi_app: fastapi.FastAPI, **limiter_args):
    app = fastapi_app()
    middleware, exception_handler = request.param
    limiter_args.setdefault("key_func", get_remote_address)
    limiter = Limiter(**limiter_args)
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, exception_handler)
    app.add_middleware(middleware)
    return app, limiter


@pytest.fixture
def test_single_decorator(self, build_fastapi_app):
    app, limiter = build_fastapi_app(key_func=get_ipaddr)
    client = TestClient(app)

    @app.get("/t1")
    @limiter.limit("5/minute")
    async def t1(request: Request):
        return PlainTextResponse("test")



@pytest.fixture
def transact(request, db):
    db.begin()
    yield
    db.rollback()