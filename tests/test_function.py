import pytest
import requests

BASE_URL = "http://<your-function-app-url>"

def test_function_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_function_response():
    response = requests.get(BASE_URL)
    assert response.text == "Hello, World!"

def test_function_edge_case():
    response = requests.get(BASE_URL, params={"name": "Jenkins"})
    assert response.status_code == 200
    assert "Hello, Jenkins!" in response.text
