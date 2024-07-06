from weather.gismeteo_weather_forecast_enums import Language
from weather.coordinates import Coordinate
from weather.location import Location
from app import load_project_dotenv
from enum import Enum
import requests
import os

CURRENT_API_URL = "https://api.gismeteo.net/v3/weather/current/"
FORECAST_API_URL = "https://api.gismeteo.net/v2/weather/forecast/"
LOCATION_API_URL = "https://api.gismeteo.net/v2/search/cities/"

load_project_dotenv()


class Encoding(Enum):
    NONE = ""
    DEFLATE = "deflate"
    GZIP = "gzip"


def _get_headers_by_encoding(encoding_type: Encoding) -> dict:
    headers = {"X-Gismeteo-Token": os.getenv("GISMETEO_TOKEN")}
    if encoding_type != Encoding.NONE:
        headers["Accept-Encoding"] = encoding_type.value
    return headers


def request_location_by_coordinates(coordinates: Coordinate, encoding_type: Encoding = Encoding.NONE,
                                    language: Language = Language.RUSSIAN) -> requests.Response:
    headers = _get_headers_by_encoding(encoding_type)
    return requests.get(
        f"{LOCATION_API_URL}?lang={language.value}&latitude={coordinates.latitude}&longitude={coordinates.longitude}&limit=1",
        headers=headers)


def request_location_by_ip(ip: str, encoding_type: Encoding = Encoding.NONE,
                           language: Language = Language.RUSSIAN) -> requests.Response:
    headers = _get_headers_by_encoding(encoding_type)
    req = requests.get(f"{LOCATION_API_URL}?lang={language.value}&ip={ip}", headers=headers)
    return req


def request_location_by_name(query: str, encoding_type: Encoding = Encoding.NONE,
                             language: Language = Language.RUSSIAN) -> requests.Response:
    headers = _get_headers_by_encoding(encoding_type)
    return requests.get(f"{LOCATION_API_URL}?lang={language.value}&query={query}&limit=1",
                        headers=headers)


def request_current_by_coordinates(coordinates: Coordinate, encoding_type: Encoding = Encoding.NONE,
                                   language: Language = Language.RUSSIAN) -> requests.Response:
    headers = _get_headers_by_encoding(encoding_type)
    return requests.get(
        f"{CURRENT_API_URL}?lang={language.value}&latitude={coordinates.latitude}&longitude={coordinates.longitude}",
        headers=headers)


def request_current_by_location(location: Location, encoding_type: Encoding = Encoding.NONE,
                                language: Language = Language.RUSSIAN) -> requests.Response:
    headers = _get_headers_by_encoding(encoding_type)
    return requests.get(f"{CURRENT_API_URL}{location.id}/?lang={language.value}",
                        headers=headers)