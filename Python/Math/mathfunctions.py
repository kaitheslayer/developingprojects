# File with the functions which will be used in math script

# Number to the power of
def po (number, pof):
    b = number
    for _ in range(pof - 1):
        b = int(b) * int(number)
    return b

# Factors of a number
def factors (number):
    current, ao, nums  = 0, 0, []
    while current < number:
        ao = ao + 1
        current = number % ao
        if current == 0:
            nums.append(ao)
    return nums

# Sqare root of number
def sqroot (number):
    fac, f = factors (number), ''
    for x in fac:
        a = x * x
        if a == number:
            return (x)
            f = True
    if f != True:
        return "No Square Root Found"
    
    
# THIS CAN SERIOUSLY BE DONE BETTER WITH CREATING OTHER FUCNTIONS, BUT LEAVING IT HERE FOR NOW...
def lineareq(numbers):
    
    ai = numbers[3]
    bi = numbers[1] * -1
    ci = numbers[2] * -1
    di = numbers[0]
    
    # Calculate the Determinent of the inverse
    
    de = ai * di - bi * ci
    
    # Calculate the final answer, for easy eye viewing
    
    xo = ai * numbers[4]
    xoo = bi * numbers[5]
    ans1 = xo + xoo
    
    xo = ci * numbers[4]
    xoo = di * numbers[5]
    ans2 = xo + xoo
    
    # Finish Equation
    ans1 = ans1 / de
    ans2 = ans2 / de
    return ans1, ans2




