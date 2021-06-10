## Learning Competencies 
 
# Your job is to build a program that will help them manage their ice cream freezing.  Here are a few user stories to help get you started:
    
# - As a ice cream maker, I want to make different types of ice cream (peanut butter, chocolate chip, etc.).
# - As a ice cream maker, I want to place batches of ice cream in an freezer.
# - As a ice cream maker, I want to know when a batch of ice cream is ready to be removed from the freezer.

### Release 0 :Design the structure

# Think about this problem critically before you even begin to write code and describe how you would design the program in plain English.
        
# At the very least, consider these questions in your answer:
        
# - What are essential classes?
# - What attributes will each class have?
# - What interface will each class provide?
# - How will the classes interact with each other?
# - Which classes will inherit from others, if any?

# Implement a minimum viable product.

# It does not need to track multiple types of ice cream, but you should be able to move ice cream into and out of a freezer.  This would be a great time to write some tests in the spec file that show how you'd _like_ your classes to work, and then get them all to pass!

#PseudoCode

# * Use composition to give structure to more complex objects

# ----- Step 1
# Icecream maker - Essential Class 
# variables: name, freezers, batches of ice cream;
# methods: order - number of batches, put in freezer, remove from freezer
#______________
# Ice cream - 
# att - types of ice cream
# methods - 
#_____________
# Freezer class - 
# vars - full or empty? storage for ice cream obj
# methods - insert ice cream, remove ice cream
#_____________

#----Step 2
# Interface
# activate ice cream maker, take in the order, process the order and put it in the freezer when completed


class IceCreamMaker:
    def __init__(self, name, freezers):
        self.name = name
        self.freezers = []
        for i in range(freezers):
            self.freezers.append(Freezer())

class IceCream:
    def __init__(self, type): 
        self.type = type

    def __str__(self):
        return self.type

class Freezer:
    def __init__(self):
        self.ice_cream = []

    def __str__(self):
        if len(self.ice_cream) > 0:
            ice_cream = self.ice_cream[0].__str__()
        else:
            ice_cream = None 
        return f"Freezer contains: {ice_cream}"
        
    def add_ice_cream(self, ice_cream):
        if len(self.ice_cream) != 0:
            return False
        else:
            self.ice_cream.append(ice_cream)
    
    def remove_ice_cream(self):
        if len(self.ice_cream) > 0:
            return self.ice_cream.pop()
        else:
            return None

my_ice_cream = IceCream("vanilla")
print(my_ice_cream)

my_freezer = Freezer()
# print(my_freezer)

my_freezer.add_ice_cream(my_ice_cream)
print(my_freezer)

my_ice_cream_2 = IceCream("chocolate")
print(my_ice_cream_2)
my_freezer.add_ice_cream(my_ice_cream_2)
print(my_freezer)

remove_ice = my_freezer.remove_ice_cream()
print(my_freezer, remove_ice)
