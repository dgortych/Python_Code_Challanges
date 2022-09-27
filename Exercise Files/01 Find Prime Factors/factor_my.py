
def get_prime_factors(num):
    res = list()
    i = 2
    while num != 1:
        if not num % i:
            res.append(i)
            num /= i
        else:
            i += 1
    return res        
        


print(get_prime_factors(0))      






