def square_digit(n):
    ch=str(n)
    s=0
    for e in ch:
        s+=int(e)**2
    return s
#print(square_digit(44))

def square_chain(n):
    m=n
    while m!=1 and m!=89:
        m=square_digit(m)
    return m
#print(square_chain(44))

def compute():
    s=0
    for i in range(1,10000000):
        if(square_chain(i)==89):
            s+=1
    return "there are",s,"numbers below",10000000,"that arrive to",89

if __name__ == "__main__": #executer compute
    print(compute())

    
    