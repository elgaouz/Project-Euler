def factoriel(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p

def curious_number(n):
    ch=str(n)
    s=0
    for e in ch:
        s+=factoriel(int(e))
    if(s==n):
        return True
    return False
#print(curious_number(145))

def sum_curious_number(n):
    s=0
    for i in range(145,n+1):
        if(curious_number(i)):
            s+=i
    return s
print(sum_curious_number(142000))
        