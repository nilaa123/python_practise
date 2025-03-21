c={'g':0}
a=['a','b','c']
b=0
c=dict.fromkeys(a,b)
print(c)
print(c.setdefault('ka',1))