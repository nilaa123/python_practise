class School:
    fees = 100
    no_of_school=0

    def __init__(self, name):
        self.name = name
        self.email = '{}@{}'.format(self.name, "gmail.com")
        School.no_of_school+=1

    def advertise(self):
        return f"Hello, welcome to {self.name}"

    def get_fees(self):
        return f"The fees for a single semester is around {self.fees}"


school_1 = School("sowma")
print(school_1.no_of_school)
school_2 = School("knms")
school_1.fees=300
print(school_1.__dict__)
# Example usage:
print(school_1.advertise())
print(school_1.get_fees())

print(school_2.advertise())
print(school_2.get_fees())
print("a")
print(school_2.no_of_school)