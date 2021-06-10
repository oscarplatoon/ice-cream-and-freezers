
import csv
import os

my_path = os.path.abspath(os.path.dirname(__file__))
flavor_path = os.path.join(my_path, "flavor.csv")

class IceCream:
    def __init__(self, flavor):
        self.flavor = flavor

    
    def list_flavors(self):
        with open(flavor_path, 'r') as flavors:
            flavor = csv.reader(flavors)
            print("\n\n             Ice cream data\n\n")
            for item in flavor:
                print(item)

    def add_flavor(self):
        list = []
        ready = 0
        flavor = input('\nEnter Flavor\n')
        time = input("\nEnter what time IceCream was added to the freezer\n")
        ready += int(time) + 500
        condition = 'good'
        with open(flavor_path, 'a', newline='') as csv_file:
            new_flavor = csv.writer(csv_file)
            list.append(flavor)
            list.append(time)
            list.append(ready)
            list.append(condition)
            new_flavor.writerow(list)


    #  need the flavor