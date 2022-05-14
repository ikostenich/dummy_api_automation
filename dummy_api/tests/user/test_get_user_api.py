import pytest
import logging as logger

from dummy_api.src.utilities.generic_utilities import generate_random_email, generate_random_string
from dummy_api.src.utilities.json_utility import extract_json


@pytest.mark.usefixtures('user_service')
class TestUser:

    pytestmark = [pytest.mark.user]

    @pytest.mark.tcid4
    @pytest.mark.smoke
    def test_get_user_required_fields(self, user_service):

        logger.debug('TEST: Create new valid user with required fields')

        payload = {
            "firstName": generate_random_string(),
            "lastName": generate_random_string(),
            "email": generate_random_email(),
            }

        created_user = user_service.create_user(**payload)

        received_user = user_service.get_user(created_user.id)

        assert created_user.first_name == received_user.first_name, f'Get user api returned wrong first_name. \
            Actual: {received_user.first_name},  Expected: {created_user.first_name}'
        assert created_user.last_name == received_user.last_name, f'Get customer api returned wrong last_name. \
            Actual: {received_user.last_name},  Expected: {created_user.last_name}'
        assert created_user.email == received_user.email, f'Get customer api returned wrong email. \
            Actual: {received_user.email},  Expected: {created_user.email}'


    @pytest.mark.tcid5
    def test_get_user_nonexistent_id(self, user_service):

        logger.debug('TEST: Create new valid user with required fields')

        EXPECTED_ERROR_TYPE = 'PARAMS_NOT_VALID'
        NONEXISTENT_ID = 'test'

        error_message = user_service.get_user(NONEXISTENT_ID, expected_status_code=400)

        actual_error_type = extract_json(error_message, '$.error')

        assert EXPECTED_ERROR_TYPE == actual_error_type, f'Error type is invalid \
            Actual: {actual_error_type},  Expected: {EXPECTED_ERROR_TYPE}'
