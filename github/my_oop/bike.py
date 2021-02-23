from datetime import datetime
from enum import Enum


class Condition(Enum):
    NEW, GOOD, OKAY, BAD = 1, 0.8, 0.5, 0.2


class MyMethodNotAllowed(Exception):
    pass


class Bike:
    count, num_wheels = 0, 2

    def __init__(self, description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost
        self.sold = False
        Bike.count += 1

    def __repr__(self):
        sold_or_price = "sold" if self.sold else f"${self.sale_price}"
        return f'Bike: {self.description} ({sold_or_price})'

    def __str__(self):
        return self.description

    def __del__(self):
        print(f'Deleting bike: {self}')
        Bike.count -= 1

    def update_sale_price(self, sale_price):
        if self.sold:
            raise MyMethodNotAllowed('Bike has already been sold')
            # raise Exception('Bike has already been sold')
        self.sale_price = sale_price

    def sell(self):
        """
        Mark as sold and determine the profit received from selling the bike
        """
        self.sold = True
        profit = self._sale_price - self.cost
        return profit

    def service(self, spent, sale_price=None, condition=None):
        """
        Service the bike and update attributes
        """
        self.cost += spent
        if sale_price:
            self.update_sale_price(sale_price)
        if self.condition:
            self.condition = condition

    @property
    def profit(self):
        if self.sold is False:
            return None
        return self.sale_price - self.cost

    @staticmethod
    def age(year):
        current_year = datetime.now().year
        age = current_year - year
        if age < 1:
            return "New"
        elif age < 5:
            return "Recent"
        elif age < 40:
            return "Old"
        else:
            return "Vintage"

    @classmethod
    def get_default_bike(cls):
        return cls(
            description="A default bike",
            condition=Condition.GOOD,
            sale_price=100
        )

    @property
    def _sale_price(self):
        return self.sale_price

    @_sale_price.setter
    def _sale_price(self, sale_price):
        if self.sold:
            raise MyMethodNotAllowed('Bike has already been sold')
        self.sale_price = sale_price

    def fun(self):
        self._sale_price = 528         # call @_sale_price.setter
        print(self._sale_price)  # call @property


# if __name__ == '__main__':

#     bike = Bike.get_default_bike()  # Class method

#     bike.sell()
#     print(bike.profit)    # Call property

#     # Call static methods
#     print(bike.age(1975))  # Vintage
#     print(Bike.age(2019))  # Recent
#     print('\n')

#       #       #       #       #       #       #       #

if __name__ == '__main__':
    bike = Bike.get_default_bike()  # Class method
    bike.fun()

    print(bike.sale_price)  # 528
    bike.sale_price = 300
    print(bike.sale_price)  # 300

    print(bike._sale_price)  # 300
    bike._sale_price = 1500
    print(bike._sale_price)  # 1500

    bike.sell()

    bike.sale_price = 200
    print(bike.sale_price, bike.sold)

    # bike._sale_price = 400  # Exception raised
