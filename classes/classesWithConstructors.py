class Point:        #'Python class' called Point
    def __init__(self,x,y):  #constructor
        self.x=x
        self.y=y

    def move(self):   #method 1
        print("move")

    def draw(self):   #method 2
        print("draw")


point1=Point(15,20)   #Created a "Instance" called Point1
point1.x=10 #attribute
point1.y=20 #attribute
point1.draw()

point2=Point(20,22) #Created a "Instance" called Point2
point2.x=1
print(point2.x)
print(point2.y)