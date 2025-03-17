def fibonacciREC(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacciREC(n-1) +fibonacciREC(n-2)