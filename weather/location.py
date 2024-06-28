from enum import Enum
from coordinates import Coordinate
from gismeteo_weather_requests import request_location_by_ip, request_location_by_name, request_location_by_coordinates
from weather.weather_forecast_enums import Language


class LocationKind(Enum):
    CITY = "T"
    METROPOLIS = "C"
    AIRPORT = "A"
    WEATHER_STATION = "M"


class Location:
    def __init__(self, ID: int, name: str, location_kind: LocationKind):
        self.__id = ID
        self.__name = name
        self.__location_kind = location_kind

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def location_kind(self) -> LocationKind:
        return self.__location_kind


def search_location_by_coordinates(coordinates: Coordinate, language: Language = Language.RUSSIAN) -> Location:
    data = request_location_by_coordinates(coordinates, language=language).json()
    return Location(data["id"], data["name"], LocationKind(data["kind"]))


def search_location_by_ip(ip: str, language: Language = Language.RUSSIAN) -> Location:
    data = request_location_by_ip(ip, language=language).json()
    return Location(data["id"], data["name"], LocationKind(data["kind"]))


def search_location_by_name(query: str, language: Language = Language.RUSSIAN) -> Location:
    data = request_location_by_name(query, language=language).json()
    return Location(data["id"], data["name"], LocationKind(data["kind"]))
