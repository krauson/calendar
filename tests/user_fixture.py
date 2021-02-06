import pytest
from sqlalchemy.orm import Session

from app.database.models import User
from tests.utils import create_model, delete_instance


@pytest.fixture
def user(session: Session) -> User:
    test_user = create_model(
        session, User,
        username='test_username',
        password='test_password',
        email='test.email@gmail.com',
<<<<<<< HEAD
=======
        language='english'
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10
    )
    yield test_user
    delete_instance(session, test_user)


@pytest.fixture
def sender(session: Session) -> User:
    sender = create_model(
        session, User,
        username='sender_username',
        password='sender_password',
        email='sender.email@gmail.com',
<<<<<<< HEAD
=======
        language='english'
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10
    )
    yield sender
    delete_instance(session, sender)
