def HCF(n,d):
    l=[i for i in range(1,n//2+1) if n%i==0]
    l1=[i for i in range(1,d//2+1) if d%i==0]
    l+=[n]
    l1+=[d]
    hcf=1
    for i in range(len(l)):
        if l[i] in l1:
            hcf=l[i]
    return hcf
#print(HCF(16,8))

def reduced_fraction_ascendant_list(m):
    l=[]
    for d in range(2,m+1):
        n=1
        while(n/d<1/2): 
            if(HCF(n,d)==1): 
                l+=[n/d]
            n+=1
    l1=sorted(l)
    return l1
#print(reduced_fraction_ascendant_list(8))

def counting_fraction_in_range(m,x,y):
    l=reduced_fraction_ascendant_list(m)
    count=0
    for i in range(len(l)):
        if(l[i]>x and l[i]<y):
            count+=1
    print(l)
    return "there are",count,"fractions between",x,"and",y
print(counting_fraction_in_range(12000, 1/3, 1/2))