# from -import -
import csv 
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/ice_cream.csv")



class IceCream:
    def __init__(self, batch_number, flavor, status):
        self.batch_number = batch_number
        self.flavor = flavor
        self.status = status

        
    @classmethod
    def all_ice_cream(cls):
        ice_cream = []

        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                print(row)
                ice_cream.append(IceCream(row[0], row[1], row[2]))
                # users.append(User(**dict(row)))

        # print(users)
        return ice_cream


    def make_batch(self, ice_cream_data):
        self.ice_cream.append(IceCream(**dict(ice_cream_data)))
        with open(path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["batch_number", "flavor", "status"])
            writer.writeheader()
            for ice_cream in self.ice_cream:
                batch_number=ice_cream.batch_number
                flavor=ice_cream.flavor
                status=ice_cream.status
                writer.writerow({"batch_number": batch_number, "flavor": flavor, "status": status})
    
    
    @classmethod # for finding users, needs updaing
    def find(self,batch_number):
        for batch in accounts:
            if account.id == str(id):
                return account
        return None


    # def update_status(self, batch_number):


# batch_number,flavor,status
# 1,RockyRoad,watery
# 2,Vanilla,watery
# 3,Chocolate,watery
