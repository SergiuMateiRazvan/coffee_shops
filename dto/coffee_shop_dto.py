class CoffeeShopDTO:
    def __init__(self, coffee_shop_name, distance):
        self._shop_name = coffee_shop_name
        self._distance = distance

    def get_distance(self):
        return self._distance

    def __str__(self):
        return f"{self._shop_name},{round(self._distance, 4)}"
