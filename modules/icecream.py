import csv
import os
from time import *
my_path = os.path.abspath(os.path.dirname(__file__))
flavor_path = os.path.join(my_path, "flavor.csv")

class IceCream:
    def __init__(self):
        pass

    
    def list_flavors(self):
        with open(flavor_path, 'r') as flavors:
            flavor = csv.reader(flavors)
            print("\n\n             Ice cream data\n\n")
            for item in flavor:
                print(item)

    def add_to_freezer(self):
        list = []
        ready = 0
        flavor = input('\nEnter Flavor\n')
        time = input("\nEnter what time IceCream was added to the freezer\n")
        ready += int(time) + 300
        condition = 'good'
        with open(flavor_path, 'a', newline='') as csv_file:
            new_flavor = csv.writer(csv_file)
            list.append(flavor)
            list.append(time)
            list.append(ready)
            list.append(condition)
            new_flavor.writerow(list)

        with open(flavor_path, 'r') as path:
            reader = csv.reader(path)

            start = process_time()
            print(f"{process_time} this is start time")
            while process_time() - start < 10:
                for item in reader:
                    if process_time() - start <= .36:#00:
                        item[3] == 'wattery'
                        print('IceCream is still wattery!')
                        continue
                    if process_time() - start > .3600 and process_time() - start <= .7200:
                        item[3] == 'almost ready'
                        print("IceCream is almost ready!")
                        continue
                    if process_time() - start > .72 and process_time() - start <= 1.0800:
                        item[3] == 'ready'
                        print("IceCream is now Ready!")
                        continue
                    if process_time() - start >= .36:
                        item[3] == 'freezer burnt'
                        return("IceCream is freezer burnt!!")
                    