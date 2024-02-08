def proper_divisors_sum(n):
    s = 1  # 1 est toujours un diviseur propre de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:# Éviter de compter deux fois le même diviseur si i != n // i
                s += n // i
    return s
#print(proper_divisors_sum(28))

def dict_sum(n):
    d={}
    for i in range(1,n):
        d[i]=proper_divisors_sum(i)
    return d
#print(dict_sum(1_000_000))

d=dict_sum(1_000_000)

def amicable_chain(n):
    #l=[n]
    m=d[n]
    mini=n
    while m!=n and m<1_000_000:
        if m>1000000:
            return []
        #l+=[m]
        if mini>m:
            mini=m
        m=d[m]
    if(m!=n):
        return 0
    else: 
        return mini
print(amicable_chain(203034))




def amicable_chain_length(n, limit=1_000_000):
    chain = set()
    while n not in chain and n < limit:
        chain.add(n)
        n = d[n]

    if n in chain:
        return len(chain) if n == chain.pop() else 0
    else:
        return 0

def smallestMember_of_longestAmicable_chain(limit=1_000_000):
    longest_chain_length = 0
    smallest_member = float('inf')

    for n in range(1, limit):
        current_chain_length = amicable_chain_length(n, limit)

        if current_chain_length > longest_chain_length:
            longest_chain_length = current_chain_length
            smallest_member = min(range(n, n + current_chain_length))

    if longest_chain_length > 0:
        print("La chaîne amicale la plus longue a une longueur de :", longest_chain_length)
        print("Plus petit nombre dans la chaîne :", smallest_member)
    else:
        print("Aucune chaîne amicale trouvée dans la plage donnée.")

#smallestMember_of_longestAmicable_chain()"""
"""def sum_of_proper_divisors(n):
    s = 1  # 1 is always a proper divisor of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s

def amicable_chain_length(n, limit=1_000_000):
    chain = set()
    while n not in chain and n < limit:
        chain.add(n)
        n = sum_of_proper_divisors(n)

    return len(chain) if n in chain else 0

def smallest_member_of_longest_amicable_chain(limit=1_000_000):
    longest_chain_length = 0
    smallest_member = float('inf')

    for n in range(1, limit):
        current_chain_length = amicable_chain_length(n, limit)

        if current_chain_length > longest_chain_length:
            longest_chain_length = current_chain_length
            smallest_member = min(range(n, n + current_chain_length))

    if longest_chain_length > 0:
        print("La chaîne amicale la plus longue a une longueur de :", longest_chain_length)
        print("Plus petit nombre dans la chaîne :", smallest_member)
    else:
        print("Aucune chaîne amicale trouvée dans la plage donnée.")

smallest_member_of_longest_amicable_chain()"""




        
    