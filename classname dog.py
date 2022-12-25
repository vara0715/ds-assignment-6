class Dog:
    def __init__(self,name,age,coat_colour):
        self.name = name
        self.age =age
        self.coat_colour = coat_colour
    
    def description(self):
        print(f"Name : {self.name} \nAge : {self.age}")

    def get_info(self):
        print(f"Coat Colour : {self.coat_colour}")

class JackRussellTerrier(Dog):
    def __init__(self,name,age,coat_colour,owner):
        super().__init__(name,age,coat_colour)
        self.owner =owner
    
    def display(self):
        print(f"Owner : {self.owner}")

class Bulldog(Dog):
    def __init__(self,name,age,coat_colour,nickname):
        super().__init__(name,age,coat_colour)
        
        self.nickname = nickname

    def view(self):
        print(f"Nick name : {self.nickname}")


jackRussellTerrier = JackRussellTerrier("whishky",2,"golden","Pratham")
jackRussellTerrier.description()
jackRussellTerrier.get_info()
jackRussellTerrier.display()

bull = Bulldog("tommy",1,"sammy","tanny")
bull.description()
bull.get_info()
bull.view()
