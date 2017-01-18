def comma(N):
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ', ' + result) if result else last3
    return result

def money(N, numwidth = 0, currency = '$'):
    sign = '-' if N<0 else ''
    N = abs(N)
    number = '{:.2f}'.format(N)
    whole = number[:-3]
    frac = number[-2:]
    whole = comma(whole)
    result = whole + '.' + frac
    return (sign or ' ') + currency + '{:>15}'.format(result) #how to add numwidth in the format?

if __name__ == '__main__':
    tests = 1, 2
    tests += 10, 101, 1123, 1234, 5345234
    for test in tests:
        print(comma(test))

    tests = 1, 2
    tests += -1, 0, -1.34534, -34534534543.0, -0.3453534, 34535345.00, -345353435.00
    for x in tests:
        print(money(x))
        
