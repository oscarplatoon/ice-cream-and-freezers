import os.path
import csv

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/icecream.csv")


class Icecream:
    ice_list = []   
    
    def __init__(self, flavor):
        self.flavor = flavor
        
    def mix_icecream():
        flavor = input("Enter flavor:\n")
        flavor.status = 0
        icecream = Icecream(flavor)
        with open(path, 'a') as csvfile:
            icecream_csv = csv.writer(csvfile)
            icecream_csv.writerow([icecream])
    
    def get_all_icecream():
        with open(path) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                    Icecream.ice_list.append(row[0])
                    
    def show_all_icecream():
        Icecream.get_all_icecream()
        for row in Icecream.ice_list:
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

    def __str__(self):
       
       return self.flavor
     