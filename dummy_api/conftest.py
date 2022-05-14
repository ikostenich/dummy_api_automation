import pytest

from dummy_api.src.services.user_service import UserService   


@pytest.fixture(scope='class')
def user_service():

    user_service = UserService()

    yield user_service
