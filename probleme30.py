def digit_fifth_power(n):
    sumfifthPowerDigit = 0
    chaine_representation = str(n)
    for e in chaine_representation:
        sumfifthPowerDigit += int(e)**5
        if sumfifthPowerDigit>n: return False
    if n == sumfifthPowerDigit:
        return True
    else:
        return False
sum = 0
for i in range(2,10000000):
   if digit_fifth_power(i):
      sum += i
print("the sum of all the numbers that can be written as the sum of fifth powers of their digits :",sum)



        
