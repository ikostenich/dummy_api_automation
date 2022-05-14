from dummy_api.src.utilities.generic_utilities import generate_random_email, generate_random_string
from dummy_api.src.utilities.requests_utility import RequestsUtility
from dummy_api.src.objects.user import User

class UserService(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_user(self, expected_status_code=200, **kwargs):
        
        kwargs = kwargs
        payload = {
            'firstName': kwargs['firstName'] if 'firstName' in kwargs.keys() else generate_random_string(),
            'lastName': kwargs['lastName'] if 'lastName' in kwargs.keys() else generate_random_string(),
            'email': kwargs['email'] if 'email' in kwargs.keys() else generate_random_email(),
        }
        payload.update(kwargs)

        create_user_json = self.requests_utility.post('user/create', payload=payload, expected_status_code=expected_status_code)
        try:
            user = User(**create_user_json)
            return user
        except TypeError:
            return create_user_json
    