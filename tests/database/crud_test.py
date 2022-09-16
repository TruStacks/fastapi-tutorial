import unittest
from unittest import mock

from mock_alchemy.mocking import AlchemyMagicMock

from fastapi_tutorial.database.models import Item, User
from fastapi_tutorial.database.schemas import ItemCreate, UserCreate
from fastapi_tutorial.database.crud import (
    get_user,
    get_user_by_email,
    get_users,
    create_user,
    get_items,
    create_user_item
)

class TestCrudMethods(unittest.TestCase):
    def test_get_user(self):
        session = AlchemyMagicMock()
        get_user(db=session, user_id=123)
        session.query().filter.assert_called_with(User.id == 123)
        session.query().filter().first.assert_called()

    def test_get_user_by_email(self):
        session = AlchemyMagicMock()
        get_user_by_email(db=session, email="test@example.com")
        session.query().filter.assert_called_with(User.email == "test@example.com")
        session.query().filter().first.assert_called()

    def test_get_users(self):
        session = AlchemyMagicMock()
        get_users(db=session, skip=1, limit=50)
        session.query().offset.assert_called_with(1)
        session.query().offset().limit.assert_called_with(50)
        session.query().offset().limit().all.assert_called()

    @mock.patch("fastapi_tutorial.database.models.User")
    def test_create_user(self, MockUser):
        session = AlchemyMagicMock()
        create_user(db=session, user=UserCreate(email="test@example.com", password="my-password!"))
        MockUser.assert_called_with(email="test@example.com", hashed_password="my-password!notreallyhashed")
        session.add.assert_called_with(MockUser())

    def test_get_items(self):
        session = AlchemyMagicMock()
        get_items(db=session, skip=5, limit=25)
        session.query().offset.assert_called_with(5)
        session.query().offset().limit.assert_called_with(25)
        session.query().offset().limit().all.assert_called()

    @mock.patch("fastapi_tutorial.database.models.Item")
    def test_create_user_item(self, MockItem):
        session = AlchemyMagicMock()
        create_user_item(db=session, item=ItemCreate(title="some title", description="some info about this item"), user_id=123)
        MockItem.assert_called_with(title="some title", description="some info about this item", owner_id=123)
        session.add.assert_called_with(MockItem())