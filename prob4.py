def ispalindromic_number(n):
    ch=str(n)
    l=[]
    for e in ch:
        l+=[e]
    for i in range(0,len(l)//2 +1):
        if(l[i]!=l[len(l)-1-i]):
            return False
    return True
#print(ispalindromic_number(9019))
            

def largestPleindrome_two_3_digit():
    l=[]
    for i in range(100,1000):
        for j in range(i,1000):
            n=i*j
            if(ispalindromic_number(n)):
                l+=[n]
    return max(l)
print(largestPleindrome_two_3_digit())