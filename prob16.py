def digit_sum(n):
    ch=str(n)
    s=0
    for e in ch:
        s+=int(e)
    return s
#print(digit_sum(16))
        
def power_digit_sum(n,a):
    p=1
    for i in range(1,a+1):
        p*=n
    return digit_sum(p)
print(power_digit_sum(2, 1000))