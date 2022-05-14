
import logging as logger
import random
import string
from datetime import datetime
from dateutil.relativedelta import relativedelta


def generate_random_email(domain=None, email_prefix=None):
    logger.debug("Generating random email and password.")

    if not domain:
        domain = 'test.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_sting_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_sting_length))

    email = f'{email_prefix}_{random_string}@{domain}'

    logger.debug(f"Randomly generated email {email}")

    return email


def generate_random_string(length=10, prefix=None, suffix=None):

    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_string = f'{prefix}{random_string}'
    if suffix:
        random_string = f'{random_string}{suffix}'

    return random_string


def generate_current_date():
    date = datetime.now() - relativedelta(years=1)
    return date.isoformat()
