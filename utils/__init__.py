import math


class UserDistanceUtils:
    def __init__(self, user_x, user_y):
        self._user_x = user_x
        self._user_y = user_y

    def get_distance_to_coffee_shop(self, coffee_shop):
        return math.sqrt(
            (self._user_x - coffee_shop.get_shop_coordinate_x()) ** 2
            + (self._user_y - coffee_shop.get_shop_coordinate_y()) ** 2
        )
