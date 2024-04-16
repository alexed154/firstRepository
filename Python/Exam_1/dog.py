class Dog:
    def __init__(self, name, trick, breed, hungry = True):
        self.name = name
        self.trick = trick
        self.breed = breed
        self.hungry = hungry
    def __str__(self):
        return "f{self.name}: {self.breed}"
    def speak(self):
        print("Woof")
    def feed(self):
        self.hungry = False
    def change_trick(self, trick):
        self.trick = trick
    def get_name(self):
        return self.name
    def get_breed(self):
        return self.breed
    def get_trick(self):
        return self.trick
    def isHungry(self):
        return self.hungry


