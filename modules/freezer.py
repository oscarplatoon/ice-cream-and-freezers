from .icecream import IceCream

class Freezer(IceCream):
    def __init__(self, flavor, time):
        super().__init__(self, flavor)
        self.time = time