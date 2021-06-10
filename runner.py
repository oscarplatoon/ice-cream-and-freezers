from ice_cream import IceCream
from freezer import Freezer

freezer = Freezer()
chocolate_icecream = IceCream('chocolate')

freezer.insert_ice_cream(chocolate_icecream)

# print(chocolate_icecream.flavor)
# print(chocolate_icecream)
# print(len(freezer.storage))

print(freezer)
print(freezer.get_ice_cream(chocolate_icecream.flavor))
print(freezer)