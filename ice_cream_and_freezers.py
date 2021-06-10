#Create single responsibility classes
#Implement clean and flexible interfaces between objects

class IceCream:
    def __init__(self, flavor, how_long_ice_cream_has_been):
        self.flavor = flavor
        self.readiness = ""
        # self.freezing_time = freezing_time
        self.how_long_ice_cream_has_been = how_long_ice_cream_has_been
        self.determine_readiness()

    def determine_readiness(self):
        if self.flavor == "chocolate":
            if self.how_long_ice_cream_has_been < 20:
                self.readiness = "watery"
            elif self.how_long_ice_cream_has_been >= 20 and self.how_long_ice_cream_has_been < 30:
                self.readiness = "almost ready"
            elif self.how_long_ice_cream_has_been >= 30 and self.how_long_ice_cream_has_been < 45:
                self.readiness = "ready"
            elif self.how_long_ice_cream_has_been >= 45:
                self.readiness = "freezer burned"
        elif self.flavor == "vanilla":
            if self.how_long_ice_cream_has_been < 30:
                self.readiness = "watery"
            elif self.how_long_ice_cream_has_been >= 30 and self.how_long_ice_cream_has_been < 40:
                self.readiness = "almost ready"
            elif self.how_long_ice_cream_has_been >= 40 and self.how_long_ice_cream_has_been < 55:
                self.readiness = "ready"
            elif self.how_long_ice_cream_has_been >= 55:
                self.readiness = "freezer burned"
        elif self.flavor == "moose_tracks":
            if self.how_long_ice_cream_has_been < 10:
                self.readiness = "watery"
            elif self.how_long_ice_cream_has_been >= 10 and self.how_long_ice_cream_has_been < 20:
                self.readiness = "almost ready"
            elif self.how_long_ice_cream_has_been >= 20 and self.how_long_ice_cream_has_been < 35:
                self.readiness = "ready"
            elif self.how_long_ice_cream_has_been >= 35:
                self.readiness = "freezer burned"
    

class Freezer:
    shared_varialbe = 0
    
    def __init__(self,time):
        self.time = time
        self.ice_creams = []

    def put_ice_cream_in_freezer(self, ice_cream):
        # implement logic to put ice cream in freezer
        self.ice_creams.append(ice_cream)

    def __str__(self):
        return f"There are {len(self.ice_creams)} ice creams currently in the freezer."

    def take_ice_cream_out_of_freezer(self, ice_cream):
        self.ice_creams.remove(ice_cream)
    
    # def time_of_freeze(self):
    #     #measure time to show the readiness

    #     for ice_cream in self.ice_creams:
    #         if self.time < 20:
    #             ice_cream.readiness = "watery"
    #         elif self.time >= 20 and self.time < 30:
    #             ice_cream.readiness = "almost ready"
    #         elif self.time >= 30 and self.time < 45:
    #             ice_cream.readiness = "ready"
    #         elif self.time >= 45:
    #             ice_cream.readiness = "freezer burned"

freezer_1 = Freezer(20)  # instantiating a new object
# freezer_1.freeze()  # methods = actions/verbs
# freezer_1.time  # instance variables = nouns/properties

chocolate = IceCream("chocolate", 30)
vanilla = IceCream("vanilla", 40)
moose_tracks = IceCream("moose_tracks", 66)
freezer_1.put_ice_cream_in_freezer(chocolate)
freezer_1.put_ice_cream_in_freezer(vanilla)
freezer_1.take_ice_cream_out_of_freezer(vanilla)
freezer_1.put_ice_cream_in_freezer(moose_tracks)
print(freezer_1)
print(freezer_1.ice_creams[0].readiness)
# print(freezer_1.time_of_freeze())
print(freezer_1.ice_creams[0].readiness)
for ice_cream in freezer_1.ice_creams:
    print(ice_cream.readiness)
print(freezer_1)


# Will you need other classes? What attributes will those classes have?
# How will classes talk to each other?
