import logging
import sys
import urllib.request

from sortedcontainers import SortedList

from domain.coffee_shop import CoffeeShop
from dto.coffee_shop_dto import CoffeeShopDTO
from utils import UserDistanceUtils

CLOSEST_SHOPS_THRESHOLD = 3
logger = logging.getLogger(__name__)


def get_coffee_shops_data(shops_url):
    shops = []
    with urllib.request.urlopen(shops_url) as f:
        shops_data = f.read().decode()

        for shop in shops_data.split("\n"):
            shop_data = shop.split(",")
            try:
                shop_name = shop_data[0]
                shop_x = float(shop_data[1])
                shop_y = float(shop_data[2])
                shops.append(CoffeeShop(shop_name, shop_x, shop_y))
            except (Exception, ValueError) as e:
                logger.warning(f"Invalid data in the coffee shops file: {e}")
                continue
    return shops


def find_closest_coffee_shop_for_user(user_coordinates, coffee_shops_data):
    distance_utils = UserDistanceUtils(*user_coordinates)
    closest_shops = SortedList(key=lambda shop: shop.get_distance())
    for coffee_shop in coffee_shops_data:
        distance = distance_utils.get_distance_to_coffee_shop(coffee_shop)
        shop_dto = CoffeeShopDTO(coffee_shop.get_shop_name(), distance)
        closest_shops.add(shop_dto)
        if len(closest_shops) > CLOSEST_SHOPS_THRESHOLD:
            closest_shops.pop()
    return closest_shops


def display_coffee_shops(coffee_shops):
    for shop in coffee_shops:
        print(shop)


def run(user_x, user_y, coffee_shops_url):
    shops_data = get_coffee_shops_data(coffee_shops_url)
    shops = find_closest_coffee_shop_for_user((user_x, user_y), shops_data)
    display_coffee_shops(shops)


if __name__ == "__main__":
    user_x = float(sys.argv[1])
    user_y = float(sys.argv[2])
    coffee_shops_url = sys.argv[3]
    run(user_x, user_y, coffee_shops_url)
