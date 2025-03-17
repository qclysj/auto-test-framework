import pytest
import requests#请求接口








@pytest.fixture(scope='module')
def mount():
    print('climb')
    yield
    print('outdoors')
# def pytest_yaml_run_step(item):
#     step=item.current_step
#     key=list(step)[0]
#     value=list(step.values)[0]
#     match key:
#         case'request':
#             resp=requests.request(**value)
#         case'response':
#             responses_validator.validator(item.resp,**value)
#     return True