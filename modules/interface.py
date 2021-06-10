from .freezer import *
from .icecream import *

class Interface():
    def __init__(self):
       pass

    def run(self):
        mode = input(self.interface_menu())
        while True:
            if mode == '1':
                return IceCream(self).list_flavors()

            elif mode == '2':
                return IceCream(self).add_flavor()

            elif mode == '3':
                pass

            elif mode == '4':
                return



        # flavor menu
       
        # ice_cream varriable freeze time

        # condition menu

    

    def interface_menu(self):
        return "\n1: List Flavor Data\n2: Add Flavor\n3: IceCream condition\n4: Exit\n\n"

        