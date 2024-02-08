def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def Goldbach_absurde():
    n = 9
    while True:
        if not is_prime(n):
            found = False
            i = 2
            while i < n:
                if is_prime(i):
                    j = 1
                    while i + 2 * (j ** 2) <= n:
                        if i + 2 * (j ** 2) == n:
                            found = True
                            break
                        j += 1
                if found:
                    break
                i += 1
            if not found:
                return n
        n += 2

print(Goldbach_absurde())





    
                    