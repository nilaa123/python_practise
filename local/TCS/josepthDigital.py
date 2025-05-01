'''Joseph is learning digital logic subject which will be for his next semester.
He usually tries to solve unit assignment problems before the lecture. 
Today he got one tricky question. The problem statement is “A positive integer has been given as an input.
Convert decimal value to binary representation. 
Toggle all bits of it after the most significant bit including the most significant bit.
Print the positive integer value after toggling all bits”.

Constrains-

1<=N<=100

Example 1:

Input :

10  -> Integer

Output :

5    -> result- Integer

Explanation:

Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”.'''

#option 1
num=int(input())
len=num.bit_length()
mask=(1<<len)-1 
toggle=num^mask
print(toggle)


''' Time complexity: O(log(N))
Space Complexity:O(1)'''









#option 2
'''
num=int(input())
result=0
i=0
while num!=0:
    res=num%2
    if res==0:
        result+=1*(2**i)
    else:
        result+=0
    i+=1
    num=num//2
print(result)
'''
