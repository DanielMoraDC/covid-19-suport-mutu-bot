from dataclasses import dataclass
from math import (
    sin,
    cos,
    sqrt,
    atan2,
    radians
)

# From https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
# Approximate radius of earth in km
R = 6373.0


@dataclass
class Location(object):

    latitude: float
    longitude: float

    def distance(self, other) -> float:
        """ Returns distance (in km) between this location and another one """
        # Parse all to radians
        lat1_radians = radians(self.latitude)
        lat2_radians = radians(other.latitude)
        long1_radians = radians(self.longitude)
        long2_radians = radians(other.longitude)

        # Compute longitude and latitude difference
        long_diff = long2_radians - long1_radians
        lat_diff = lat2_radians - lat1_radians

        # Apply formula
        a = sin(lat_diff / 2)**2 + cos(lat1_radians) * cos(lat2_radians) * sin(long_diff/ 2)**2  # noqa
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return R * c
