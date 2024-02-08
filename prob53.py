def factoriel(n):
    if n==0:
        return 1
    fct=1
    for i in range(1,n+1):
        fct*=i
    return fct
#print(factoriel(4))

def combinator(r,n):
    if(r<=n):
        return factoriel(n)//(factoriel(r)*factoriel(n-r))
#print(combinator(3,5))

def combinatoric_Selections():
    count=0
    for n in range(1,101):
        for r in range(1,n+1):
            if(combinator(r, n)>1_000_000):
                count+=1
    return count
print(combinatoric_Selections())
                
        