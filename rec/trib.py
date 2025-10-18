d = {1:1,2:1,3:1}
def tribonacci(n):
    result = d.get(n)
    if result is None:
        result =tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
        d[n]=result
    return result        
print(tribonacci(7))
print(tribonacci(1))
print(tribonacci(4))