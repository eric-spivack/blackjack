import os
import pytest
import json
from datetime import datetime, timedelta
from functools import wraps
from unittest.mock import patch
 
def mock_decorator(f):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)
        return decorated_function
    return decorator
 
def pytest_configure():
    pytest.VERSION_NUMBER = '1.1.1'
    pytest.NAME = 'blahblah'

@pytest.fixture
def app():
    #patch('app.api.oauth.oauth_required.oauth_required', lambda x: x).start()
    os.environ['VERSION_NUMBER'] = pytest.VERSION_NUMBER
    os.environ['NAME'] = pytest.NAME
    #from app.api.app_server import create_app
    #app = create_app('')
    #app.debug = True
    return {}
 