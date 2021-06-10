class IceCream:
    def __init__(self, flavor):
        self.flavor = flavor
        self.done_status = "watery"
        
    def __str__(self):
        return f"Ice Cream Flavor: {self.flavor} is in freeze status: {self.done_status}"

    def get_flavor(self):
        return self.flavor
    def get_done_status(self):
        return self.done_status

    def set_done_status(self, changed_doneness):
        self.done_status = changed_doneness

#- As a ice cream maker, I want to make different types of ice cream (peanut butter, chocolate chip, etc.).
    # Ice cream has types/flavors that age differently, Peanut Butter, Chocolate Chip, Vanilla, Strawberry
    # Maybe some kind of batch ID? Churn Freeze Status? 
    # Churn Freeze Status: