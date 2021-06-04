class IceCream:
    def __init__(self, name, freezing_time):
        self.name = name
        self.freezing_time = freezing_time
        self.status = ""
        self.update_status()

    def update_status(self):
        if self.freezing_time >= 2:
            self.status = "watery"
        elif self.freezing_time == 1:
            self.status = "almost_ready"
        elif self.freezing_time == 0:
            self.status = "ready"
        else:
            self.status = "freezer_burned"


class Freezer:
    def __init__(self):
        self.ice_creams = []  # will contain IceCream instances

    def put(self, ice_cream):
        self.ice_creams.append(ice_cream)

    def remove(self, ice_cream_name):
        for ice_cream in self.ice_creams:
            if ice_cream.name == ice_cream_name:
                self.ice_creams.remove(ice_cream)

    def return_ice_cream(self):
        arr_to_return = []
        for ice_cream in self.ice_creams:
            ice_cream.update_status()
            arr_to_return.append((ice_cream.name, ice_cream.status))
        return arr_to_return

    def freeze(self):
        for ice_cream in self.ice_creams:
            ice_cream.freezing_time -= 1
            ice_cream.update_status()


fr = Freezer()
choco = IceCream("Chocolate", 3)
vanil = IceCream("Vanilla", 2)

fr.put(choco)
fr.put(vanil)
print(fr.return_ice_cream())
