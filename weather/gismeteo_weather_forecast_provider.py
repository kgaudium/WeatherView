from datetime import datetime

from gismeteo_weather_requests import request_current_by_location
from weather.location import Location
from weather_forecast_provider import WeatherForecastProvider
from weather_forecast_enums import *


class GismeteoWeatherForecastProvider(WeatherForecastProvider):
    def __init__(self):
        self.__location: Location = None
        self.__language: Language = None
        self._provider_response: dict = None

    @property
    def location(self) -> Location:
        return self.__location

    @location.setter
    def location(self, location: Location) -> None:
        self.__location = location

    @property
    def language(self) -> Language:
        return self.__language

    @language.setter
    def language(self, language: Language) -> None:
        self.__language = Language(language)

    def update_forecast(self):
        r = request_current_by_location(self.location, language=self.language)
        self._provider_response = r.json()

    @property
    def forecast_kind(self) -> ForecastKind:
        return ForecastKind(self._provider_response["kind"])

    @property
    def data_date(self) -> datetime:
        date_string = self._provider_response["date"]["local"]
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    @property
    def air_temperature(self) -> float:
        return self._provider_response["temperature"]["air"]

    @property
    def water_temperature(self) -> float:
        return self._provider_response["temperature"]["water"]

    @property
    def feels_like_temperature(self) -> float:
        return self._provider_response["temperature"]["comfort"]

    @property
    def weather_description(self) -> str:
        return self._provider_response["description"]["full"]

    @property
    def humidity(self) -> int:
        return self._provider_response["humidity"]["percent"]

    @property
    def pressure(self) -> int:
        return self._provider_response["pressure"]["mm_hg_atm"]

    @property
    def cloudiness_percent(self) -> int:
        return self._provider_response["cloudiness"]["percent"]

    @property
    def cloudiness_type(self) -> CloudinessType:
        return CloudinessType(self._provider_response["cloudiness"]["type"])

    @property
    def is_storm_predicted(self) -> bool:
        return self._provider_response["storm"]["prediction"]

    @property
    def precipitation_type(self) -> PrecipitationType:
        return PrecipitationType(self._provider_response["precipitation"]["type"])

    @property
    def precipitation_amount(self) -> float | None:
        return self._provider_response["precipitation"]["amount"]

    @property
    def precipitation_intensity(self) -> PrecipitationIntensity:
        return PrecipitationIntensity(self._provider_response["precipitation"]["intensity"])

    @property
    def geomagnetic_field_intensity(self) -> GeomagneticFieldIntensity:
        return GeomagneticFieldIntensity(self._provider_response["gm"])

    def get_icon_file_name(self) -> str:
        # TODO
        raise NotImplementedError("get_icon_file_name method not implemented yet")

    @property
    def wind_direction_in_degrees(self) -> int:
        return self._provider_response["wind"]["direction"]["degree"]

    @property
    def wind_direction_scale_8(self) -> WindScale8:
        return WindScale8(self._provider_response["wind"]["direction"]["scale_8"])

    @property
    def wind_speed(self) -> float:
        return self._provider_response["wind"]["speed"]["m_s"]
