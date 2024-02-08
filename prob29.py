def distinct_power(a,b):
    l=[]
    for i in range(2,a+1):
        for j in range(2,b+1):
            if not(pow(i, j) in l):
                l+=[pow(i, j)]
    return len(l)
print(distinct_power(100, 100))