def sum_squeres(n):
    s=0
    for i in range(1,n+1):
        s+=i**2
    return s

def squere_sum(n):
    p=0
    for i in range(1,n+1):
        p+=i
    return p**2

def difference(n):
    return squere_sum(n)-sum_squeres(n)

print(difference(100))
