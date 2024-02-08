def factoriel(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
#print(factoriel(6))

def digit_factoriel_chain(n):
    ch=str(n)
    digit_factoriel=0
    for e in ch: 
        digit_factoriel+=factoriel(int(e))
    return digit_factoriel
#print(digit_factoriel_chain(169))

def longueur_of_non_repeating_chain(n):
    l=[]
    l.append(n)
    m=digit_factoriel_chain(n)
    while m not in l:
        l.append(m)
        m=digit_factoriel_chain(m)
    return len(l)
#print(longueur_of_non_repeating_chain(69))

def number_of_chains(x):
    n=1
    s=0
    while(n<x):
        if(longueur_of_non_repeating_chain(n)==60):
            s+=1
        n+=1
    return "there are",s,"chains with a starting number\
        below",x,"that contain exactly 60 non repeating terms"
print(number_of_chains(1000000))
            
