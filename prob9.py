def pythagorean_triplet(a,b,c):
    if(a<b and b<c):
        if(a**2 + b**2 == c**2):
            return True
        return False
    return False
#print(pythagorean_triplet(3, 4, 5))

def findPythagorean():
    b=2
    while(b<1000): 
        for a in range(1,b):
            c=1000-a-b
            if(pythagorean_triplet(a, b, c)):
                return "the product of the pythagorean triplet a:",a,"b:",b,"c:",c,"is",a*b*c
        b+=1

print(findPythagorean())
        

