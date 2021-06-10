

class IceCream:

    def __init__(self, flavor, status = 'ready'):
        self.flavor = flavor
        self.status = status
    
    def __str__(self) -> str:
        return self.flavor