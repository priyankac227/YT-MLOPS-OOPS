#initiate a class
class employee:
    # special method/ magic method /dunder method -constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.desigantion = "SDE"
    
    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")


#create an obj/instance of the class
sam = employee()
#print(sam.id)
sam.travel()