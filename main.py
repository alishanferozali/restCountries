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
        # print(json.dumps(countries_data,indent=4))

        # Running this api to get all the data  of  rest countries.
        north_american_countries_data = requests.get("https://restcountries.com/v3.1/all").json()

        # Filter countries from the continent "North America"
        north_american_countries = [country for country in north_american_countries_data if 'North America' in country.get('continents', [])]

        # Uncomment below statement to print all data for countries in the North American Continent in json format.
        print(json.dumps(north_american_countries,indent=4))


        # Running this api to get us all calling codes for countries in the Americas.
        calling_codes=requests.get("https://restcountries.com/v3.1/region/Americas?fields=idd").json()

        # Uncomment below statement to print calling keys with idd.root and idd.suffixes for countries in the Americas.
        # print(json.dumps(calling_codes, indent=4))


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
    rest_countries_api()
    #ApiUser()


