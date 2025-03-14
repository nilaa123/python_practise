class Mammal:#parent class
    def walk(self):
        print("walking")


class dog(Mammal):
    def bark(self):
        print("bow bow")


class cat(Mammal):
    def meow(self):
        print("meowwww")


shiro=dog()
shiro.bark()
shiro.walk()