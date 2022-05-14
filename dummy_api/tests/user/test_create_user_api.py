import pytest
import logging as logger
import random

from dummy_api.src.utilities.generic_utilities import generate_random_email, generate_random_string, generate_current_date
from dummy_api.src.utilities.json_utility import extract_json


@pytest.mark.usefixtures('user_service')
class TestUser:

    pytestmark = [pytest.mark.user]

    @pytest.mark.tcid1
    @pytest.mark.smoke
    def test_create_user_smoke(self, user_service):

        logger.debug('TEST: Create new valid user with required fields')

        payload = {
            "firstName": generate_random_string(),
            "lastName": generate_random_string(),
            "email": generate_random_email(),
            }

        user = user_service.create_user(**payload)

        assert user.first_name == payload['firstName'], f'Create user api returned wrong first_name. \
            Actual: {user.first_name},  Expected: {payload["firstName"]}'
        assert user.last_name == payload['lastName'], f'Create customer api returned wrong last_name. \
            Actual: {user.last_name},  Expected: {payload["lastName"]}'
        assert user.email == payload['email'], f'Create customer api returned wrong email. \
            Actual: {user.email},  Expected: {payload["email"]}'


    @pytest.mark.tcid2
    def test_create_user_full(self, user_service):

        logger.debug('TEST: Create new valid user with all fields')
        payload = {
            "title": random.choice(("mr", "ms", "mrs", "miss", "dr")),
            "firstName": generate_random_string(),
            "lastName": generate_random_string(),
            "gender": random.choice(("male", "female", "other")),
            "email": generate_random_email(),
            "dateOfBirth": generate_current_date(),
            "phone": generate_random_string(),
            "picture": generate_random_string(),
        }


        user = user_service.create_user(**payload)

        assert user.first_name == payload['firstName'], f'Create user api returned wrong first_name. \
            Actual: {user.first_name},  Expected: {payload["firstName"]}'
        assert user.last_name == payload['lastName'], f'Create customer api returned wrong last_name. \
            Actual: {user.last_name},  Expected: {payload["lastName"]}'
        assert user.email == payload['email'], f'Create customer api returned wrong email. \
            Actual: {user.email},  Expected: {payload["email"]}'


    @pytest.mark.tcid3
    def test_verify_invalid_email_error_message(self, user_service):

        logger.debug('TEST: Create new valid user with invalid email. Verify fields.')
        
        payload = {
            "email": generate_random_string(),
            }
        
        EXPECTED_ERROR_TYPE = 'BODY_NOT_VALID'
        expected_error_message = f'Path `email` is invalid ({payload["email"]}).'

        error_message = user_service.create_user(expected_status_code=400, **payload)
        
        actual_error_type = extract_json(error_message, '$.error')
        actual_error_message = extract_json(error_message, '$.data.email')


        assert EXPECTED_ERROR_TYPE == actual_error_type, f'Error type is invalid \
            Actual: {actual_error_type},  Expected: {EXPECTED_ERROR_TYPE}'
        assert expected_error_message == actual_error_message, f'Error message type is invalid \
            Actual: {actual_error_message},  Expected: {expected_error_message}'
