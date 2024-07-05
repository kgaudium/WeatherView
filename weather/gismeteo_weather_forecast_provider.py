from datetime import datetime

from weather.gismeteo_weather_requests import request_current_by_location
from weather.location import Location
from weather.weather_forecast_provider import WeatherForecastProvider
from weather.gismeteo_weather_forecast_enums import *


def get_wind_direction_name(scale8: WindScale8) -> str:
    match scale8:
        case WindScale8.NORTH:
            return "С"
        case WindScale8.NORTHEAST:
            return "СВ"
        case WindScale8.EAST:
            return "В"
        case WindScale8.SOUTHEAST:
            return "ЮВ"
        case WindScale8.SOUTH:
            return "Ю"
        case WindScale8.SOUTHWEST:
            return "ЮЗ"
        case WindScale8.WEST:
            return "З"
        case WindScale8.NORTHWEST:
            return "СЗ"
        case WindScale8.CALM:
            return "Ш"
        case _:
            return "Н/Д"


def get_geomagnetic_field_intensity_name(intensity: GeomagneticFieldIntensity) -> str:
    match intensity:
        case GeomagneticFieldIntensity.NO_DISTURBANCE:
            return "Нет заметных возмущений"
        case GeomagneticFieldIntensity.MINOR_DISTURBANCE:
            return "Небольшие возмущения"
        case GeomagneticFieldIntensity.WEAK_STORM:
            return "Слабая геомагнитная буря"
        case GeomagneticFieldIntensity.MINOR_STORM:
            return "Малая геомагнитная буря"
        case GeomagneticFieldIntensity.MODERATE_STORM:
            return "Умеренная геомагнитная буря"
        case GeomagneticFieldIntensity.STRONG_STORM:
            return "Сильная геомагнитная буря"
        case GeomagneticFieldIntensity.SEVERE_STORM:
            return "Жесткий геомагнитный шторм"
        case GeomagneticFieldIntensity.EXTREME_STORM:
            return "Экстремальный шторм"


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
        r = request_current_by_location(self.location, language=self.language).json()
        if r["meta"]["status_code"] != 200:
            raise Exception("Cannot update forecast")

        self._provider_response = r["data"]

    @property
    def forecast_kind(self) -> ForecastKind:
        return ForecastKind(self._provider_response["kind"])

    @property
    def data_date(self) -> datetime:
        date_string = self._provider_response["date"]["local"]
        return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")

    @property
    def air_temperature(self) -> float:
        value = self._provider_response["temperature"]["air"]["C"]
        if value is None:
            return "Н/Д"

        return value

    @property
    def water_temperature(self) -> float:
        value = self._provider_response["temperature"]["water"]["C"]
        if value is None:
            return "Н/Д"

        return value

    @property
    def feels_like_temperature(self) -> float:
        value = self._provider_response["temperature"]["comfort"]["C"]
        if value is None:
            return "Н/Д"

        return value

    @property
    def weather_description(self) -> str:
        value = self._provider_response["description"]
        if value is None:
            return "Н/Д"

        return value

    @property
    def humidity(self) -> int:
        value = self._provider_response["humidity"]["percent"]
        if value is None:
            return "Н/Д"

        return value

    @property
    def pressure(self) -> int:
        value = self._provider_response["pressure"]["mm_hg_atm"]
        if value is None:
            return "Н/Д"

        return value

    @property
    def cloudiness_percent(self) -> int:
        return self._provider_response["cloudiness"]["percent"]

    @property
    def cloudiness_type(self) -> CloudinessType:
        return CloudinessType(self._provider_response["cloudiness"]["scale_3"])

    @property
    def is_storm_predicted(self) -> bool:
        value = self._provider_response["storm"]["prediction"]
        if value is None:
            return "Н/Д"

        return value

    @property
    def precipitation_type(self) -> PrecipitationType:
        value = PrecipitationType(self._provider_response["precipitation"]["type"])
        if value is None:
            return "Н/Д"

        return value

    @property
    def precipitation_amount(self) -> float | None:
        value = self._provider_response["precipitation"]["amount"]
        if value is None:
            return "Н/Д"

        return value

    @property
    def precipitation_intensity(self) -> PrecipitationIntensity:
        return PrecipitationIntensity(self._provider_response["precipitation"]["intensity"])

    # @property
    # def geomagnetic_field_intensity(self) -> GeomagneticFieldIntensity:
    #     return GeomagneticFieldIntensity(self._provider_response["gm"])

    def get_icon_file_name(self) -> str:
        return self._provider_response["icon"]["icon-weather"]

    @property
    def wind_direction_in_degrees(self) -> int:
        value = self._provider_response["wind"]["direction"]["degree"]
        if value is None:
            return "Н/Д"

        return value

    @property
    def wind_direction_scale_8(self) -> WindScale8:
        value = self._provider_response["wind"]["direction"]["scale_8"]
        if value is None:
            return "Н/Д"

        return WindScale8(value)

    @property
    def wind_speed(self) -> float:
        value = self._provider_response["wind"]["speed"]["m_s"]
        if value is None:
            return "Н/Д"

        return value
