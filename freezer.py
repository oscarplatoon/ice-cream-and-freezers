from ice_cream import IceCream

class Freezer: #inherited freezer classes for different icecream types?

    def __init__(self, size = 20):
        self.storage = []
        self.size = size

    def __str__(self):
        temp = 'FREEZER CONTENTS: '
        for s in self.storage:
            temp += str(s) + "\n"
        return temp

    # Runs a freeze cycle which increments cycles on every IceCream object by 1
    def freeze_ice_cream(self):
        for ice_cream in self.storage:
            freezer_cycles = ice_cream.get_freezer_cycles()
            freezer_cycles += 1
            ice_cream.set_freezer_cycles(freezer_cycles)
        return self.storage

    # Adds Ice Cream
    def store_ice_cream(self, flavor):
        if len(self.storage) >= self.size:
            raise Exception("The freezer is full!")
        ice_cream = IceCream(flavor) 
        self.storage.append(ice_cream)
        return self.storage

    def remove_first_ice_cream(self):
        if len(self.storage) == 0:
            raise Exception("Freezer is Empty.")
        # Remove the first ice cream you see
        return self.storage.pop()
    
    def remove_ice_cream_by_status(self, flavor, status):
        desired_ice_cream_status = status
        for index, ice_cream in enumerate(self.storage):
            if ice_cream.get_flavor() == flavor and desired_ice_cream_status == ice_cream.return_status():
                return self.storage.pop(index)
        raise Exception("You haven't found the ice cream you're looking for.")
        
    # - As a ice cream maker, I want to place batches of ice cream in an freezer.
    #- As a ice cream maker, I want to know when a batch of ice cream is ready to be removed from the freezer.
    # Stores Ice Cream Objects
    # Freezer has a repeatable "Freeze" method that advances the ice cream through the states of freezing:
    # watery, almost_ready, ready, over_churned, butter
    # Freezer flavor types? Strawberry icecream freezer, CC IC freezer, PB IC freezer...?
    # Strawberry : 2 age per advance of doneness
    # Chocolate Chip: 1 per advance
    # Vanilla: 4 per advance
    # PB: 3 per advance
