# from -import -
import csv 
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/freezer.csv")

from classes.ice_cream import IceCream

class Freezer:

    def __init__(self,in_freezer):
        super().__init__(batch_number, flavor, status,)
        self.in_freezer = 'y'

    def __str__(self):
        return f"""
        Batch_number: {self.batch_number}
        Flavor: {self.flavor}
        Status: {self.status}
        """

    @classmethod
    def all_freezer(cls):
        ice_cream_freezer = []

        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                print(row)
                ice_cream_freezer.append(IceCream(row[0], row[1], row[2], row[3]))
                # users.append(User(**dict(row)))

        # print(users)
        return ice_cream_freezer


    # def into_freezer(self, ice_cream):
    #     print(ice_cream.flavor)
    #     self.ice_cream.append(ice_cream)
    #     with open(path, 'w', newline='') as csv_file:
    #         writer = csv.DictWriter(csv_file, fieldnames = ["batch_number", "flavor", "status"])
    #         writer.writeheader()
    #     for ice_cream in self.ice_cream:
    #         batch_number=ice_cream.batch_number
    #         flavor=ice_cream.flavor
    #         status=ice_cream.status
    #         writer.writerow({"batch_number": batch_number, "flavor": flavor, "status": status})


    #     for ice_cream in self.ice_cream:
    #         if ice_cream.batch_number == batch_number:
    #         freezer_inv.append()
    #     print('map')