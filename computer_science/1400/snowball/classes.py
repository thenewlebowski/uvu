class Dog:
    def __init__(self, name, breed):
        self.breed = breed
        self.name = name
    def bark(self):
        return "bark bark"
    def speak(self):
        return "my name is {self.name}"

dog = Dog("doug", "pit bull")

print(dog.breed)
print(dog.bark())
print(dog.speak())

class Game:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def whatGame(self):
        print("Option 3 is " + self.name)

g1 = Game("Super Mario Galaxy", "AAA")
g2 = Game("Cuphead", "indie")
g3 = Game("Hollow Knight", "indie")

g3.whatGame()

class Person:
    def __init__(self, food, hobby):
        self.food = food
        self.hobby = hobby

    def fav(self):
        print("My favorite food is "+ self.food)
    def myhobby(self):
        print ("I like to do " + self.hobby + " in my free time")

num1 = Person("stawberries", "coding")

num1.fav()
num1.myhobby()



