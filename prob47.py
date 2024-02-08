def est_premier(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
#print(est_premier(14))
def inclu_list(n):
  c=0
  for i in range(2,n):
    if est_premier(i) and n%i==0:
      c+=1
  return c
#print(inclu_list(644))
r=134040
while True:
  c1=inclu_list(r)
  c2=inclu_list(r+1)
  c3=inclu_list(r+2)
  c4=inclu_list(r+3)
  if c1==4 and c2==4 and c3==4 and c4==4:
    break
  r+=1
print(r)