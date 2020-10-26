import requests


class GeoInsightFetcher:
    def __init__(self, api_url="https://restcountries.eu/rest/v2/"):
        self.api_url = api_url

    def get_city_info_by_name(self, name):
        city_url = f"{self.api_url}capital/{name}/"
        response = requests.get(city_url)
        if response:
            if response.status_code == 200:
                data = response.json()[0]
                city = {
                    "Country": data.get("name"),
                    "Currency": data.get("currencies")[0].get("code"),
                }
                return city
