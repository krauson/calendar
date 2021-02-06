from fastapi.testclient import TestClient
import pytest

<<<<<<< HEAD
from app.database.models import User
from app.main import app
from app.database.database import Base
from app.routers import profile, agenda, invitation
from tests.conftest import test_engine, get_test_db
=======
from app import main
from app.database.database import Base
from app.database.models import User
from app.main import app
from app.routers import agenda, event, invitation, profile
from tests.conftest import get_test_db, test_engine
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


<<<<<<< HEAD
@pytest.fixture(scope="session")
def agenda_test_client():
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[agenda.get_db] = get_test_db
=======
def create_test_client(get_db_function):
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[get_db_function] = get_test_db
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10

    with TestClient(app) as client:
        yield client

    app.dependency_overrides = {}
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="session")
<<<<<<< HEAD
def invitation_test_client():
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[invitation.get_db] = get_test_db

    with TestClient(app) as client:
        yield client

    app.dependency_overrides = {}
    Base.metadata.drop_all(bind=test_engine)
=======
def agenda_test_client():
    yield from create_test_client(agenda.get_db)


@pytest.fixture(scope="session")
def invitation_test_client():
    yield from create_test_client(invitation.get_db)


@pytest.fixture(scope="session")
def home_test_client():
    yield from create_test_client(main.get_db)


@pytest.fixture(scope="session")
def event_test_client():
    yield from create_test_client(event.get_db)
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10


@pytest.fixture(scope="session")
def profile_test_client():
    Base.metadata.create_all(bind=test_engine)
    app.dependency_overrides[profile.get_db] = get_test_db
    app.dependency_overrides[
        profile.get_placeholder_user] = get_test_placeholder_user

    with TestClient(app) as client:
        yield client

    app.dependency_overrides = {}
    Base.metadata.drop_all(bind=test_engine)


def get_test_placeholder_user():
    return User(
        username='fake_user',
        email='fake@mail.fake',
        password='123456fake',
<<<<<<< HEAD
        full_name='FakeName'
=======
        full_name='FakeName',
        telegram_id='666666'
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10
    )
