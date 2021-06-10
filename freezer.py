from ice_cream import IceCream

class Freezer:
    def __init__(self):
        self.storage = []

    def age_ice_cream(self):
        pass

    def store_ice_cream(self, flavor):
        #IceCream objects come from the freezer? Different class of ice-cream-producer?
        if len(self.storage) > 20:
            raise Exception("The freezer is full!")
        ice_cream = IceCream(flavor) 
        self.storage.append(ice_cream)
        return self.storage

    def remove_first_ice_cream(self):
        if len(self.storage) == 0:
            raise Exception("Freezer is Empty.")
        # Remove the first ice cream you see
        return self.storage.pop()
    
    def remove_done_ice_cream(self, flavor, doneness):
        for index, ice_cream in enumerate(self.storage):
            if ice_cream.get_flavor() == flavor and ice_cream.get_done_status():
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