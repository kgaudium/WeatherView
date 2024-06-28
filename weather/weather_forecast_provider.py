from weather.location import Location
from weather_forecast_enums import *
import datetime
import abc


class WeatherForecastProvider(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def location(self):
        pass

    @location.setter
    @abc.abstractmethod
    def location(self, location: Location) -> None:
        pass

    @property
    @abc.abstractmethod
    def forecast_kind(self) -> ForecastKind:
        pass

    @property
    @abc.abstractmethod
    def data_date(self) -> datetime.datetime:
        pass

    @property
    @abc.abstractmethod
    def air_temperature(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def water_temperature(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def feels_like_temperature(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def weather_description(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def humidity(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def pressure(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def cloudiness_percent(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def cloudiness_type(self) -> CloudinessType:
        pass

    @property
    @abc.abstractmethod
    def is_storm_predicted(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def precipitation_type(self) -> PrecipitationType:
        pass

    @property
    @abc.abstractmethod
    def precipitation_amount(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def precipitation_intensity(self) -> PrecipitationIntensity:
        pass

    @property
    @abc.abstractmethod
    def geomagnetic_field_intensity(self) -> GeomagneticFieldIntensity:
        pass

    @abc.abstractmethod
    def get_icon_file_name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def wind_direction_in_degrees(self) -> int:
        pass

    @property
    @abc.abstractmethod
    def wind_direction_scale_8(self) -> WindScale8:
        pass

    @property
    @abc.abstractmethod
    def wind_speed(self) -> float:
        pass
