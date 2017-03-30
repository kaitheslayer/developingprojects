# File with the functions which will be used in math script


def po (number, pof):
    b = number
    for _ in range(pof - 1):
        b = int(b) * int(number)
    return b

def factors (number):
    current, ao, nums  = 0, 0, []
    while current < number:
        ao = ao + 1
        current = number % ao
        if current == 0:
            nums.append(ao)
    return nums

def sqroot (number):
    fac, f = factors (number), ''
    for x in fac:
        a = x * x
        if a == number:
            return (x)
            f = True
    if f != True:
        return "No Square Root Found"



