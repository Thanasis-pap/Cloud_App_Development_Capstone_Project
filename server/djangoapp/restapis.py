import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth


def get_request(url, **kwargs):
    print(kwargs)
    try:
        if "apikey" in kwargs:
            response = requests.get(url, headers={
                                    'Content-Type': 'application/json'}, params=kwargs, auth=HTTPBasicAuth("apikey", kwargs["apikey"]))
        else:
            response = requests.get(
                url, headers={'Content-Type': 'application/json'}, params=kwargs)
        status_code = response.status_code
        print("With status {} ".format(status_code))
        json_data = json.loads(response.text)
    except Exception as e:
        print("Error ", e)
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

def post_request(url, json_payload, **kwargs):
    print(json_payload)
    print("POST from {} ".format(url))
    try:
        response = requests.post(url, params=kwargs, json=json_payload)
        status_code = response.status_code
        print("With status {} ".format(status_code))
        json_data = json.loads(response.text)
        print(json_data)
        return json_data
    except:
        print("Network exception occurred")


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



