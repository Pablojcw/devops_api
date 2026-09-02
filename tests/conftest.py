import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

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
