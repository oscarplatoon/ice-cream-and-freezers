from .icecream import IceCream
import csv
import os
import time

my_path = os.path.abspath(os.path.dirname(__file__))
flavor_path = os.path.join(my_path, "flavor.csv")

class Freezer(IceCream):
    def __init__(self):
        super().__init__(self)
        self.time = 0
        
    def check_condition(self):
        condition_dict = {
            1: 'wattery',
            2: 'almost ready',
            3: 'ready',
            10: 'freezer_burned'
        }
        flavor_to_check = input("\nEnter Flavor to check condition of\n...")
        with open(flavor_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for icecream in reader:
                if flavor_to_check == icecream[0]:
                    pass
                else:
                    print(f"You Have no more More {flavor_to_check} left in stock!")
