import numpy as np
import pytest


@pytest.fixture
def generate_data_for_tests():
    data = {
            "p_res": 250,
            "wct": 50,
            "pi": 1,
            "pb": 150,
        }
    return data


def test_calc_model_success(api_client, generate_data_for_tests):
    response = api_client.post('http://127.0.0.1:8002/ipr/calc', json=generate_data_for_tests)
    assert response.status_code == 200
    assert response.json
