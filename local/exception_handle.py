a,b=-1,2
if a<0:
    raise ValueError("no negative")
try:
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("one more try because",e,"occured")
except TypeError as e:
    print(e)
finally:
    print("resource closed")