''' It determines the GCD of two numbers'''


def gcd(a,b):
    #a, b = abs(a), abs(b) 
    reminder=a%b
    if reminder==0:
        return b
    else:
        return gcd(b,reminder)

print(gcd(123456, 789012))
