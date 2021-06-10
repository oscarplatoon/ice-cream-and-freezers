class IceCream:
    chocolate_dict = {
        0: 'watery',
        1: 'almost_ready',
        2: 'ready',
        3: 'over_churned',
        4: 'butter'
    }

    vanilla_dict = {
        0: 'watery',
        1: 'almost_ready',
        2: 'almost_ready',
        3: 'almost_ready',
        4: 'almost_ready',
        5: 'ready',
        6: 'over_churned',
        7: 'butter'
    }

    strawberry_dict = {
        0: 'watery',
        1: 'almost_ready',
        2: 'ready',
        3: 'ready',
        4: 'ready',
        5: 'over_churned',
        6: 'butter'
    }

    peanut_butter_dict = {
        0: 'watery',
        1: 'almost_ready',
        2: 'ready',
        3: 'over_churned',
        4: 'butter'
    }

    status = ""
    def __init__(self, flavor):
        self.flavor = flavor
        self.freezer_cycles = 0
        # self.status = ""
        
    def __str__(self):
        return f"Ice Cream Flavor: {self.flavor} is in freeze status: {self.freezer_cycles}"

    # Getters
    def get_flavor(self):
        return self.flavor
    def get_freezer_cycles(self):
        return self.freezer_cycles
    def get_doneness(self):
        return self.doneness

    # Setters
    def set_freezer_cycles(self, freezer_counter):
        self.freezer_cycles = freezer_counter
    def set_doneness(self, doneness):
        self.doneness = doneness

    # Compares freezer cycles to class defined dictionary for a given flavor
    # Returns a str status of watery, almost ready, ready, over_churned, or butter
    def return_status(self):
        status = ""
        flavor = self.get_flavor()
        status_dict = {}
        freezer_cycles = self.get_freezer_cycles()
        if flavor == "Chocolate":
            status_dict = self.chocolate_dict
        elif flavor == "Vanilla":
            status_dict = self.vanilla_dict
        elif flavor == "Peanut Butter":
            status_dict == self.peanut_butter_dict
        elif flavor == "Strawberry":
            status_dict == self.strawberry_dict
        # Thought of the day: If the above works, it's not that wrong.
        status += status_dict[freezer_cycles]
        return status
