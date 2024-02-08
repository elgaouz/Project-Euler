def sum_of_proper_divisors(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s+=i
    return s
#print(sum_of_proper_divisors(220))

def amicable_numbers(n):
    l=[]
    for i in range(1,n+1):
        if i not in l: 
            s1=sum_of_proper_divisors(i)
            if(i==sum_of_proper_divisors(s1) and (i!=s1)): #ie amicables
                l+=[i]+[s1]
    s=sum(l)
    return "the sum of all amicable numbers under",n,": ",s
print(amicable_numbers(10000))
        
        
    
