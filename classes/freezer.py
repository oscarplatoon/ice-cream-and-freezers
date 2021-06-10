import os
import csv
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/icecream.csv")

class Freezer:
    # Freezes icecream put in
    # Keeps track of how long icecream has been in
    # (Notifies user when icecream is done freezing?)
    def __init__(self):
        self.icecream_in_freezer = []
    
    def get_all_freezer():
        with open(path) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                    Freezer.ice_list.append(row[0])
                    
    def show_all_freezer():
        Freezer.get_all_icecream()
        for row in Freezer.ice_list:
            print(row)
        input("\nHit Enter to to return")

    def show_icecream():
        Icecream.get_all_icecream()
        flavor = input("Enter icecream flavor:  ")
        for row in Icecream.ice_list:
            if row == flavor:
                print(row)
                input("\nHit Enter to continue")
                return
        print("Flavor not found!")
        input("\nHit Enter to continue")
 
    def add_freezer():
        pass
    