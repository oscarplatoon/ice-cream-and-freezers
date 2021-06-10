class IceCream:
    def __init__(self, flavor, change_time, batch):
        self.flavor = flavor 
        self.time = 0
        self.change_status_time = change_time 
        self.state = 'watery'
        self.batch = batch


class Freezer:
    ice_cream_timer ={
        'chocolate' : 1,
        'strawberry' : 2,
        'vanilla' : 3
    }
    states = ['watery','almost_ready','ready','freezer_burned']
    
    def __init__(self):
    #Initialize freezer
        self.storage = []

    def wait_one_hour(self):
    # Increment hour, update states of all flavors/batches in freezer
        for x in self.storage:
            x.time += 1
            if x.time == x.change_status_time and x.state != 'freezer_burned':
                x.state = self.states[self.states.index(x.state)+1]
                x.time = 0

    def check_freezer(self):
    #print all contents of freezer for flavor, batch, and state
        for x in self.storage:
            return(f'Flavor: {x.flavor}\tBatch: {x.batch}\tState: {x.state}')


class IceCreamMaker:
    def make_ice_cream(self,flavor):
        batch_list = []

        if flavor in self.ice_cream_timer.keys():
            change_time = self.ice_cream_timer[flavor]
        else:
            return(f'\nFlavor not in recognized!\n')
            
        for x in self.storage:
            if x.flavor == flavor:
                batch_list.append(x.batch)
        batch = 1
        while batch in batch_list:
            batch += 1
        self.storage.append(IceCream(flavor, change_time,batch))
        
       

    def use_ice_cream(self,flavor):
        for x in self.storage:
            if x.state == 'ready' and x.flavor == flavor:
                self.storage.pop(self.storage.index(x))
                return(f"batch number {x.batch} of {x.flavor} is now {x.state}. Removing now...")
                



