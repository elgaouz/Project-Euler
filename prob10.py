def is_prime(n):
    for i in range(2,int(n**(0.5)+1)):
        if(n%i==0):
            return False
    return True 

def sum_primes_below(n):
    s=0
    for p in range(2,n):
        if(is_prime(p)):
            s+=p
    return 'the sum of primes below ',n,' : ',s

print(sum_primes_below(2000000))
