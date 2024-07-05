import json

from weather.gismeteo_weather_forecast_enums import Language
from weather.location import Location
from weather.gismeteo_weather_forecast_provider import (GismeteoWeatherForecastProvider, get_wind_direction_name,
                                                        get_geomagnetic_field_intensity_name)


def get_weather_json(location: Location):
    provider = GismeteoWeatherForecastProvider()
    provider.location = location
    provider.language = Language.RUSSIAN

    provider.update_forecast()
    data = {
        "name": location.name,
        "temp": str(provider.air_temperature) if provider.air_temperature <= 0 else '+' + str(provider.air_temperature),
        "feels": str(provider.feels_like_temperature) if provider.feels_like_temperature <= 0 else '+' + str(provider.feels_like_temperature),
        "icon_name": provider.get_icon_file_name(),
        "desc": provider.weather_description,
        "date": provider.data_date.strftime("%d %B %Y, %H:%M"),
        "wind_speed": provider.wind_speed,
        "wind_scale8": get_wind_direction_name(provider.wind_direction_scale_8),
        "wind_degrees": provider.wind_direction_in_degrees,
        "pressure": provider.pressure,
        "humidity": provider.humidity,
        # "gm": get_geomagnetic_field_intensity_name(provider.geomagnetic_field_intensity),
        "water": str(provider.water_temperature) if provider.water_temperature <= 0 else '+' + str(provider.water_temperature),
    }

    return json.dumps(data)
