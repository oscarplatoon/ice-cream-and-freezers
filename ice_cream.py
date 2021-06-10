class IceCream:
    chocolate_dict = {
        0: 'watery',
        1: 'almost_ready',
        2: 'ready',
        3: 'over churned',
        4: 'butter'
    }

    vanilla_dict = {
        0: 'watery',
        1: 'almost_ready',
        2: 'almost_ready',
        3: 'almost_ready',
        4: 'almost_ready',
        5: 'ready',
        6: 'over churned',
        7: 'butter'
    }

    strawberry_dict = {
        0: 'watery',
        1: 'almost_ready',
        2: 'ready',
        3: 'ready',
        4: 'ready',
        5: 'over churned',
        6: 'butter'
    }

    peanut_butter_dict = {
        0: 'watery',
        1: 'almost_ready',
        2: 'ready',
        3: 'over churned',
        4: 'butter'
    }

    status = ""
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

    """WIP Build Have a set_dictionary method that determines which key/freezer cycle to use for determining status?"""
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
