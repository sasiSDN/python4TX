import pytest
import allure
import requests

@allure.title("Test create booking CURD Positive")
@allure.description("TC#1 Verify test request invalid")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url="https://restful-booker.herokuapp.com"
    path_url="/booking"
    URL=base_url+path_url
    headers={"Content-Type":"application/json"}
    payload={
        "firstname": "Susan",
        "lastname": "Wilson",
        "totalprice": 416,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2020-01-13",
            "checkout": "2023-04-05"
        }
    }
    response=requests.post(url=URL,headers=headers,json=payload)
    assert response.status_code==200
    response_data=response.json()
    bookingid=response_data["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid)==int


    firstname=response_data["booking"]["firstname"]
    lastname=response_data["booking"]["lastname"]
    totalprice=response_data["booking"]["totalprice"]
    depositpaid=response_data["booking"]["depositpaid"]
    assert firstname=="Susan"
    assert lastname=="Wilson"
    assert totalprice==416
    assert depositpaid==False


    check_in=response_data["booking"]["bookingdates"]["checkin"]
    check_out = response_data["booking"]["bookingdates"]["checkout"]
    assert check_in=="2020-01-13"
    assert check_out=="2023-04-05"


@allure.title("Test create booking CURD Positive")
@allure.description("TC#2 Booking  is not created with {} data")
@pytest.mark.crud
def test_create_booking_positive_tc2():
    base_url="https://restful-booker.herokuapp.com"
    path_url="/booking"
    URL=base_url+path_url
    headers={"Content-Type":"application/json"}
    json_payload={}
    response = requests.post(url=URL, headers=headers, json=payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))
    assert response.status_code==500


@allure.title("Test create booking CURD Positive")
@allure.description("TC#2 verify booking with total price with string")
@pytest.mark.crud
def test_create_booking_positive_tc3():
    base_url="https://restful-booker.herokuapp.com"
    path_url="/booking"
    URL=base_url+path_url
    headers={"Content-Type":"application/json"}
    payload={
        "firstname": "Susan",
        "lastname": "Wilson",
        "totalprice": sa,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2020-01-13",
            "checkout": "2023-04-05"
        }
    }
    response=requests.post(url=URL,headers=headers,json=payload)


