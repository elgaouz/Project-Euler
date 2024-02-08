def digit_sum(n):
    ch=str(n)
    s=0
    for e in ch:
        s+=int(e)
    return s

def factoriel_digit_sum(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return digit_sum(p)
print(factoriel_digit_sum(100))