from framework.base.config_class import Config
import requests
import base64
import json
import pytest


@pytest.mark.parametrize("login, password", [("user", "password")])
def test_basic_auth(login, password):
    login_and_pass = (login + ':' + password).encode('utf-8')
    base64_login_and_pass = base64.b64encode(login_and_pass).decode('utf-8')

    headers = {
        'Authorization': 'Basic ' + base64_login_and_pass
    }

    response = requests.get(Config().get_url(), headers=headers)
    result = json.loads(response.content.decode('utf-8'))
    assert result["authenticated"] is True and result["user"] == "user", "Wrong response to authentication request"
