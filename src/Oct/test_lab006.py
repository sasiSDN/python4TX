# PUT - Request
# URL
# Path - Booking ID
# Token - Auth
# Payload
# Headers

import allure
import pytest
import requests


# Create Token - POST
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username":"admin",
        "password":"password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token=response.json()["token"]
    print(token)
    return token

#create booking - POST
def create_booking():
    URL="https://restful-booker.herokuapp.com/booking"
    headers={"Content-Type":"application/json"}
    payload={
        "firstname": "Susan",
        "lastname": "Wilson",
        "totalprice":144,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2020-01-13",
            "checkout": "2023-04-05"
        }
    }
    response=requests.post(url=URL,headers=headers,json=payload)
    print(type(URL))
    print(type(headers))
    print(type(payload))
    # Assertions
    assert response.status_code == 200
    # get the reponse Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


def test_put_request_positive():
    base_url="https://restful-booker.herokuapp.com"
    path_url="/booking/"+str(create_booking())
    PUT_URL = base_url+path_url
    cookie="token="+create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie":cookie
    }
    json_payload = {
        "firstname": "Susan",
        "lastname": "Wilson",
        "totalprice":144,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2020-01-13",
            "checkout": "2023-04-05"
        }
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Susan"
def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    response = requests.delete(url=DELETE_URL, headers=headers)