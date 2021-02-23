from bike import Bike, Condition

bike1 = Bike(description='Univega Alpina, orange',
             condition=Condition.OKAY,
             sale_price=500,
             cost=100)

bike1.service(sale_price=600, spent=30)  # cost=$130, sale_price=$600

print(bike1)
print(bike1.sale_price)                  # 600
print(bike1.sell())                      # 470, sold=True

#       #       #       #       #       #       #       #

bike2 = Bike('Univega Alpina, orange',
             Condition.OKAY, sale_price=500, cost=100)

print(bike2)        # __str__ called
print(str(bike2))   # __str__ called

print([bike2])      # __repr__ called
print(repr(bike2))  # __repr__ called

#       #       #       #       #       #       #       #

print(bike2.num_wheels)     # 2
# print(bike1.num_wheels)     # 2
print(Bike.num_wheels)     # 2

print(Bike.count)  # 2

del bike1
print(Bike.count)  # 1
# (bike2)All Objects are auto deleted when program finishes.
