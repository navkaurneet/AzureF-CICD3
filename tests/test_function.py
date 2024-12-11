import pytest
import requests

BASE_URL = "https://nav-python-function-app.azurewebsites.net/api/http_trigger1?code=y4_qSWtSo87aNMMNx5CMNb0oSsWcvk8QBtJzkCESDYX8AzFuwIdHiw%3D%3D"

def test_function_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_function_default_response():
    response = requests.get(BASE_URL)
    assert response.text == (
        "This HTTP triggered function executed successfully. This is the assignment3 Azure Function Pipeline."
    )

def test_function_with_name_param():
    response = requests.get(BASE_URL, params={"name": "Jenkins"})
    assert response.status_code == 200
    assert "Hello, Jenkins. This HTTP triggered function executed successfully." in response.text

def test_function_invalid_json():
    response = requests.post(BASE_URL, json={"invalid": "data"})
    assert response.status_code == 200
    assert (
        "This HTTP triggered function executed successfully. This is the assignment3 Azure Function Pipeline."
        in response.text
    )
