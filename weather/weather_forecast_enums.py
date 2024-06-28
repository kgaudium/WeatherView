from enum import Enum


class Language(Enum):
    ENGLISH = "en"
    RUSSIAN = "ru"
    UKRAINIAN = "ua"
    LITHUANIAN = "lt"
    LATVIAN = "lv"
    POLISH = "pl"
    ROMANIAN = "ro"


class ForecastKind(Enum):
    OBSERVE = "Obs"
    FORECAST = "Frc"


class CloudinessType(Enum):
    CLEAR = 0
    PARTLY_CLOUDY = 1
    CLOUDY = 2
    OVERCAST = 3
    VARIABLE_CLOUDINESS = 101


class PrecipitationType(Enum):
    NONE = 0
    RAIN = 1
    SNOW = 2
    MIXED = 3


class PrecipitationIntensity(Enum):
    NONE = 0
    LIGHT = 1
    MODERATE = 2
    HEAVY = 3


class GeomagneticFieldIntensity(Enum):
    NO_DISTURBANCE = 1
    MINOR_DISTURBANCE = 2
    WEAK_STORM = 3
    MINOR_STORM = 4
    MODERATE_STORM = 5
    STRONG_STORM = 6
    SEVERE_STORM = 7
    EXTREME_STORM = 8


class WindScale8(Enum):
    CALM = 0
    NORTH = 1
    NORTHEAST = 2
    EAST = 3
    SOUTHEAST = 4
    SOUTH = 5
    SOUTHWEST = 6
    WEST = 7
    NORTHWEST = 8
