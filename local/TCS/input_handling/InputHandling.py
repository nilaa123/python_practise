# Case 1: [1,2,3,4,5]

def case_1():
    list1=list(map(int,input().strip("[]").split(",")))
    return list1

# Case 2: 1 2 3 4 5
def case_2():
    list1=list(map(int,input().split(' ')))
    print(list1)

#Case 3: 1,2,3,4,5
def case_3():
    list1=list(map(int,input().split(',')))
    print(list1)

