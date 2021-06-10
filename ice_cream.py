class IceCream:
  
    easy_dict = {
    6: "freezer_burned",
    4: "ready",
    2: "almost_ready",
    0: "watery"
    }
    med_dict = {
    8: "freezer_burned",
    6: "ready",
    4: "almost_ready",
    0: "watery"
    }
    hard_dict = {
    10: "freezer_burned",
    8: "ready",
    6: "almost_ready",
    0: "watery"
    }

        
    # flavor is a string i.e. -> 'chocolate'
    # time_in_freezer is int -> 0 -> infinity
    # status is int -> corresponds to 

    def __init__(self, flavor, difficulty = 'e',status = 'watery',time_in_freezer = 0):
        self.flavor = flavor
        self.status = status
        self.difficulty = difficulty
        self.time_in_freezer = time_in_freezer
    
    def __str__(self) -> str:
        return f"""Flavor: {self.flavor}\nStatus: {self.status}\n"""
    
    #setter for time
    def set_time_in_freeze(self, time):
        self.time_in_freezer = time

    #loop through time/status dict to update status
    def update_status(self):
        if self.difficulty == 'e':
            ice_dict = IceCream.easy_dict
        elif self.difficulty == 'm':
            ice_dict = IceCream.med_dict
        elif self.difficulty == 'h':
            ice_dict = IceCream.hard_dict
        else:
            raise Exception("No other difficulty") 
        for x in ice_dict:
            if self.time_in_freezer >= x:
                self.status = ice_dict[x]
                break
        return self.status
        