import pytest
import allure
import requests

@allure.title("Test GET request- Restful BOOKER project#1")
@allure.description("Verify GET request with ID works")
@allure.tag("regression", "p0", "smoke")
# @allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "sasi naidu")
# @allure.link("", name="Website")
# @allure.issue("AUTH-123")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url="https://restful-booker.herokuapp.com/booking/1"
    response_data=requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code==200

@allure.title("Test GET request- Restful BOOKER project#2")
@allure.description("TC#2 Verify test request invalid")
@pytest.mark.smoke
def test_get_single_request_by_id_negative_1():
    url="https://restful-booker.herokuapp.com/booking/-1"
    response_data=requests.get(url)
    assert response_data.status_code==404


@allure.title("Test GET request- Restful BOOKER project#3")
@allure.description("TC#3 Verify test request invalid")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url="https://restful-booker.herokuapp.com/booking/invalid"
    response_data=requests.get(url)
    assert response_data.status_code==404