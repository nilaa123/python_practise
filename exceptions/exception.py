#The prevention of exit code 1

try:
    age=int(input("age:"))
    income=500
    risk=age/income
    print(age)
except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print("Only natural numbers allowed")