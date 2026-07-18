import pytest

@pytest.fixture(params=['in prog', 'done'])
def request_input(request):
    return request.param


def test_fixture_param(request_input: list[str]):
    assert request_input in ['in prog', 'done']
