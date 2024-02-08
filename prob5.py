def smallest_multiple(n):
    m=5
    done=False
    while(done==False):
        for i in range(1,n+1):
            if m%i!=0:
                break
                m=m+1
                done=False

    return m
print(smallest_multiple(3))
