from ice_cream import IceCream
from freezer import Freezer

freezer = Freezer()
chocolate_icecream = IceCream('chocolate')
pb_ice = IceCream('Peanut_Butter', 'm')
delish_ice = IceCream('Delish', 'h')

freezer.insert_ice_cream(chocolate_icecream)
freezer.insert_ice_cream(pb_ice)
freezer.insert_ice_cream(delish_ice)
print(freezer)

for ice in freezer.storage:
    ice.set_time_in_freeze(6)
    ice.update_status()
    if ice.status == 'ready':
        print("I'm going to eat", freezer.remove_ice(ice), "ice cream")

# print(freezer)

