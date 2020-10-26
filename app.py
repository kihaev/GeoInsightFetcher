from src.geo_insight_fetcher import GeoInsightFetcher
from src.utils import read_file, read_cli
import sys


api_url = "https://restcountries.eu/rest/v2/"

default_cities = ["Kiev", "London"]


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Running with default cities")
        print()
        cities = default_cities

    elif sys.argv[1] == "-f":
        cities = read_file(sys.argv[2])

    else:
        cities = read_cli(sys.argv[1:])

    if cities:
        for city in cities:
            print(f"  {city.title()}")
            print("-------------")

            api = GeoInsightFetcher(api_url=api_url)
            city_info = api.get_city_info_by_name(city.lower())

            if city_info:
                for key, value in city_info.items():
                    print(key + ": " + value)
            else:
                print("  Invalid City Name")

            print("-------------")
            print()
