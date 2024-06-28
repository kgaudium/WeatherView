def check_if_correct_latitude(latitude: float) -> bool:
    return -90 < latitude < 90


def check_if_correct_longitude(longitude: float) -> bool:
    return -180 < longitude < 180


def _raise_exception_if_wrong_latitude(latitude: float) -> None:
    if check_if_correct_latitude(latitude):
        return
    raise ValueError(f"Latitude must be between -90 and 90 degrees. Given {latitude}")


def _raise_exception_if_wrong_longitude(longitude: float) -> None:
    if check_if_correct_longitude(longitude):
        return
    raise ValueError(f"Longitude must be between -180 and 180 degrees. Given {longitude}")


class Coordinate:
    def __init__(self, latitude: float = None, longitude: float = None):
        _raise_exception_if_wrong_latitude(latitude)
        _raise_exception_if_wrong_longitude(longitude)

        self.__latitude = latitude
        self.__longitude = longitude

    @property
    def latitude(self) -> float:
        return self.__latitude

    @property
    def longitude(self) -> float:
        return self.__longitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        _raise_exception_if_wrong_latitude(latitude)
        self.__latitude = latitude

    @longitude.setter
    def longitude(self, longitude: float) -> None:
        _raise_exception_if_wrong_longitude(longitude)
        self.__longitude = longitude

