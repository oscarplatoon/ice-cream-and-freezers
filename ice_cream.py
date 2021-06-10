class IceCream:
    def __init__(self, flavor):
        self.flavor = flavor
        self.freezer_cycles = 0
        
    def __str__(self):
        return f"Ice Cream Flavor: {self.flavor} is in freeze status: {self.freezer_cycles}"

    def get_flavor(self):
        return self.flavor
    def get_freezer_cycles(self):
        return self.freezer_cycles
    def get_doneness(self):
        return self.doneness

    def set_freezer_cycles(self, freezer_counter):
        self.freezer_cycles = freezer_counter
    def set_doneness(self, doneness):
        self.doneness = doneness

    # Different flavors having different donenesses. Might be worthwhile to have the ice_cream know how done it is?
    # No doneness at init, assigned a doneness based on their flavor/freezer_cycles

    def return_status(self):
        pass
#- As a ice cream maker, I want to make different types of ice cream (peanut butter, chocolate chip, etc.).
    # Ice cream has types/flavors that age differently, Peanut Butter, Chocolate Chip, Vanilla, Strawberry
    # Maybe some kind of batch ID? Churn Freeze Status? 
    # Churn Freeze Status: