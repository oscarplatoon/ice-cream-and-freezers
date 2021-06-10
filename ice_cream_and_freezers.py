from classes.icecream import Icecream
from classes.freezer import Freezer
import time

class Icecream_tracker():
    def __init__(self):
        self.icecreams = []
        self.runner()
# User interface
    def runner(self):
        while True:
            mode = input("\nWhat would you like to do?\nOptions:\n1. Enter new icecream\n2. Show all icecream\n3. Search icecream\n4. Place icecream in freezer\n5. Remove icecream from freezer\n6. Show all icecream in freezer\n9. Quit\n")
            if mode == '1':
                Icecream.mix_icecream()
            elif mode == '2':
                Icecream.show_all_icecream()
            elif mode == '3':
                Icecream.show_icecream()
            elif mode == '4':
                Freezer.add_icecream()
            elif mode == '5':
                Freezer.remove_icecream()
            elif mode == '6':
                Freezer.show_icecream()
            elif mode == '9':
                print("Exiting program")
                time.sleep(1)
                break  


# Freezer.add_icecream()
# Interface
        # 1. Add New Icecream
        # 2. Show all icecream
        # 3. Put Icecream in Freezer
        # 4. Pull Icecream from Freezer