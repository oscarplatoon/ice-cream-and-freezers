from ice_cream import IceCream

class Freezer:
    max_storage = 10


    def __init__(self, size = max_storage):
       self.storage = []
       self.size = size
        # all_ice_cream = IceCream.objects()

    def __str__(self) -> str:
        temp = 'FREEZER CONTENTS: \n-----------\n'

        for s in self.storage:
            temp += str(s) + "\n"
        return temp
        


    def insert_ice_cream(self, new_ice_cream):
        self.storage.append(new_ice_cream)

    def get_ice_cream(self, flavor):
        for ice_cream in self.storage:
            if ice_cream.flavor == flavor:
                self.storage.remove(ice_cream)
                return ice_cream