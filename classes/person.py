class Person:
    def __init__(self,name):
        self.name=name
    

    def talk(self):
        print(f"hello,this is {self.name}")


john=Person("john kathir")
john.talk()
Mason=Person("Mason parker")
Mason.talk()