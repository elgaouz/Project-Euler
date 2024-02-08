
def is_prime(n):
    for i in range(2,int(n**(0.5)+1)):
        if(n%i==0):
            return False
    return True 
#print(is_prime(18))
"""
def primeFactors(n):
    for i in range(2,n):
        if(i%2!=0): 
            if (n%i==0 and is_prime(i)): 
                print(i,"is a prime factor of ",n)
print(primeFactors(13195))"""

#more optimised
def primeFactors(n):
        while(not(is_prime(n))):
            for p in range(2,n):
                if(n%p==0 and is_prime(p)):
                    print(p,"is a prime factor of n")
                    n=n//p
                    print("n : ",n)
        
        
print(primeFactors(600851475143))

    
            
