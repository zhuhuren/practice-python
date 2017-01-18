def isprime(num):
    from math import sqrt
    type_num = type(num)
    if type_num == int or type_num == float:
        num_abs = abs(num)
        if num == int(num):
            divisor = 2 if type_num == int else 2.0
            num_sqrt = sqrt(num)
            while divisor <= num_sqrt:
                if num % divisor == 0:
                    print(num, 'has a factor', divisor, '.')
                    break
                divisor += 1
            else: print(num, 'is a prime number.')
        else: print(num, 'isn\'t a whole number, so it\'t not a prime number.')
    else: print("'", num, "'", 'isn\'t a number, so it\'s not a prime number.')

# isprime(46536252425671417377931) note: this is a prime number
