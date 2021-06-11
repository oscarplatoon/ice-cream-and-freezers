import csv 
import os.path

from classes.ice_cream import IceCream
from classes.freezer import Freezer

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/freezer.csv")


class Interface:
    def __init__(self, name):
        self.name = name
        self.ice_cream = IceCream.all_ice_cream()
        self.ice_cream_freezer = Freezer.all_freezer()
        self.ice_cream_menu()

    def ice_cream_menu(self):
        while True:
            user_input = int(input("""

            1. Make Batch of Ice cream.
            2. Place Ice cream in freezer.
            3. Take Ice cream batch from freezer.
            4. Check status of Ice cream batches.
            5. 1 hour time elapse.
            6. Quit

            """))
            if user_input == 1:
                self.make_batch()
            elif user_input == 2:
                self.into_freezer()
            elif user_input == 3:
                self.takeout_freezer()           
            elif user_input == 4:
                self.Status_ice_cream()            
            elif user_input == 5:
                self.time_lapse()
            elif user_input == 6:
                break

    def make_batch(self):
        ice_cream_data = {'flavor': 'batch_number'}

        ice_cream_data['flavor'] = input("\n\nWhat flavor of icecream would you like to make?\n\n")
        ice_cream_data['batch_number'] = input("\n\nWhat batch number is this?\n\n")
        ice_cream_data['status'] = 'watery'

        IceCream.make_batch(self,ice_cream_data)
        print('you just created xxxx batch')

    def into_freezer(self):
        
                
        #         return batches
                with open(path, 'w', newline='') as csv_file:
                    writer = csv.DictWriter(csv_file, fieldnames = ["batch_number", "flavor", "status","in_freezer"])
                    writer.writeheader()
                    batch_number = input('What Batch Number would you like to put into the freezer?')
                    if len(self.ice_cream) == 0:
                        print("Your are out of icecream")
                    for batch in self.ice_cream:
                        if batch.batch_number == batch_number:
                            self.ice_cream_freezer.append(batch)
                            batch_number=batch.batch_number
                            flavor=batch.flavor
                            status=batch.status
                            in_freezer= "y"
                            writer.writerow({"batch_number": batch_number, "flavor": flavor, "status": status,"in_freezer": in_freezer})
                
                # 
                # print (f'Batches in the freezer are: {self.freezer_inv}')

               

    # def time_lapse(self):

        
