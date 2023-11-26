from math import radians, sin, cos, sqrt, atan2


class CoordinatesChecker():
    """
        Checks the Given Coordinates or within the range of 30 miles of radius.
    """

    def check(self, request, format=None):
        """
            Check if lat long exists in range. #user input is 12.7194995, 80.048614
        """
        able_to_check_in = self.check_if_lat_long_exists_in_range(
            12.7194995, 80.048614)
        status = "failure"
        if able_to_check_in:
            status = "success"
        return Response({"status": status})

    def check_if_lat_long_exists_in_range(self, user_lat, user_long, dock=None):
        dock_lat = float("13.0787031")
        dock_long = float("80.2542044")
        return self.haversine(dock_lat, dock_long, user_lat, user_long, 30)

    def haversine(self, dock_lat, dock_long, user_lat, user_long, radius_miles=30):
        # Radius of Earth
        R = 3959.0

        # Convert lat long from degree to radius
        dock_lat_radius, dock_long_radius, user_lat_radius, user_long_radius = map(radians,
                                                                                   [dock_lat, dock_long, user_lat,
                                                                                    user_long])

        # Calculate the differences between latitudes and longitudes
        distance_of_latitude = user_lat_radius - dock_lat_radius
        distance_of_longitude = user_long_radius - dock_long_radius

        # Haversine formula
        a = sin(distance_of_latitude / 2) ** 2 + cos(dock_lat_radius) * cos(user_lat_radius) * sin(
            distance_of_longitude / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Calculate the distance
        distance = R * c
        return distance <= radius_miles
