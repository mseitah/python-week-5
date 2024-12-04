class Gadgets:
    def __init__ (self,brand:str,price:int):
        self.brand=brand
        self.price=price

class smartPhones(Gadgets):
    def make_call(self, number):
        return f"Calling {number} from {self._brand} {self.model}"
    
IPhone=smartPhones("apple", 300)

print(IPhone.brand)
print(IPhone.make_call(1234567890))

#assignment 2

class Grasshopper:
    def move(self):
        return "Hop"
    
class Bird:
    def move(self):
        return "flying"
    
class Fish:
    def move(self):
        return "swim"
    
for animal in [Grasshopper(),Bird(),Fish()]:
    print(animal.move())
        