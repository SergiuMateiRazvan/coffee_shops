class CoffeeShop:
    def __init__(self, shop_name, shop_coordinate_x, shop_coordinate_y):
        self._shop_name = shop_name
        self._shop_coordinate_x = shop_coordinate_x
        self._shop_coordinate_y = shop_coordinate_y

    def get_shop_name(self):
        return self._shop_name

    def get_shop_coordinate_x(self):
        return self._shop_coordinate_x

    def get_shop_coordinate_y(self):
        return self._shop_coordinate_y
