from gettext import install

import locust as locust
import requests
from locust import HttpUser, task, between
import json


def rest_countries_api():
    try:
        # Running this api to get all the data for countries in the North America Region.
        countries_data=requests.get("https://restcountries.com/v3.1/subregion/North America").json()

        # Uncomment below statement to print all data for countries in the North American Region in json format.
        #print(json.dumps(countries_data,indent=4))


        # Running this api to get us all calling codes for countries in the Americas.
        calling_codes=requests.get("https://restcountries.com/v3.1/region/Americas?fields=idd").json()

        # Uncomment below statement to print calling keys with idd.root and idd.suffixes for countries in the Americas.
        # print(json.dumps(calling_codes, indent=4))

        # Below statement will extract all the suffixes from idd object
        suffixes = [data['idd']['suffixes'] for data in calling_codes]

        # Uncomment below statement to print only calling codes(suffixes) for countries in the Americas in json format.
        #print(json.dumps(suffixes, indent=4))

        # Below statement will flatten the list of suffixes so that it comes in one array
        calling_codes_suffixes = [item for sublist in suffixes for item in sublist]

        # Uncomment below statement to print only calling codes(suffixes) for countries in the Americas.
        #print(calling_codes_suffixes)

    except Exception as exception:
        print({str(exception)})


class ApiUser(HttpUser):
    wait_time = between(1, 3)  # Simulates user wait time between requests

    @task
    def test_api(self):
        response = self.client.get("/")  # API Endpoint
        if response.status_code == 200:
            print("Request Successful")
        else:
            print(f"Request Failed: {response.status_code}")


if __name__ == '__main__':
    ApiUser()

