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

    # Different flavors having different donenesses. Might be worthwhile to have the ice_cream know how done it is?
    # No doneness at init, assigned a doneness based on their flavor/freezer_cycles

    """WIP Build Have a set_dictionary method that determines which key/freezer cycle to use for determining status?"""
    # def return_status(self):
    #     status_dict = {}
    #     if self.get_flavor() == "Chocolate":
    #         status_dict = chocolate_dict
    #     elif self.get_flavor() == "Vanilla":
    #         status_dict = vanilla_dict
    #     flavor = self.get_flavor()
    #     freezer_cycles = self.get_freezer_cycles()


        #ice_cream.status = ice_cream.return_status()
        return status
        pass
# test = IceCream("Vanilla")
# print(test.return_status())