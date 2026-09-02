import pytest

from app.main import create_monitoring_TI


@pytest.fixture
def app(tmp_path):
    database = tmp_path / "test.db"

    app = create_monitoring_TI({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{database}",
    })

    yield app


@pytest.fixture
def client(app):
    return app.test_client()