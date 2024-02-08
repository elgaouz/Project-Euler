def devided_by_all(m,n):
    for i in range(1,n+1):
        if(m%i!=0):
            return False
    return True
               

def smallest_evenly_divisible(n):
    m=n
    while(not devided_by_all(m, n)):
        m+=n
    return "the smallest positive number divided by numbers from 1 to",n,":",m
        
print(smallest_evenly_divisible(20))