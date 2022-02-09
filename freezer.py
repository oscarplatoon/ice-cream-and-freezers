class Freezer:


    def __init__(self):
       self.storage = []

    def __str__(self) -> str:
        temp = 'FREEZER CONTENTS: \n-----------------\n'
        if self.storage == []:
            temp += "Empty"
        for s in self.storage:
            temp += str(s) + "\n"
        return temp
        
    def insert_ice_cream(self, new_ice_cream):
        self.storage.append(new_ice_cream)

    def get_ice_cream(self):
        ice_list = []
        for ice_cream in self.storage:
            ice_list.append((ice_cream.flavor,ice_cream.status))
        return ice_list

    def remove_ice(self, ice_cream):
        self.storage.remove(ice_cream)
        return ice_cream.flavor
    
    def list_freeze_contents(self, num):
        
        for ice in self.storage:
            ice.set_time_in_freeze(num)
            ice.update_status()
            if ice.status == 'ready':
                print(f"The {ice.flavor} ice cream is ready to be taken out of the freezer")
                print(f"I'm going to eat the {self.remove_ice(ice)} ice cream")