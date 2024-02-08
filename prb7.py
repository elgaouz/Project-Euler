def is_prime(n):
    for i in range(2,int(n**(0.5)+1)):
        if(n%i==0):
            return False
    return True

def max_primeNumber_under(n):
    l=[]
    m=len(l)
    p=2
    while(m<n):
        if(is_prime(p)):
            l+=[p]
            m+=1
            p+=1
        p+=1
    return l[-1]
        
print(max_primeNumber_under(10000))
            
    
