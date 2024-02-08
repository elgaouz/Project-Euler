def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
def list_prime(p):
    T=[]
    for i in range(2,10000006):
        if prime(i):
            T=T+[i]
    return T[p-1]
print(list_prime(10001))