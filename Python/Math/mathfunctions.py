# File with the functions which will be used in math script


# ========================================================================= Non Math Functions
def tnuml(n):
    o = []
    for _ in n:
        _ = float(_)
        o.append(_)
    return o
# ========================================================================= Non Math Functions

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
    

# Linear Patern Solver    
def lseq (ls1, ls2, ls3, ls4):
    if int(ls2) - int(ls1) == int(ls4) - int(ls3):
        lsd1 = int(ls2) - int(ls1)  # common difference
        lsc = int(lsd1) - int(ls1)  # constant e.g. Tn = xn + c
        lsc = int(lsc) * -1
        if lsd1 == 1:  # added to change Tn = 1n to Tn = n
            return("Tn = %sn+" % (lsd1) + ("%s" % (lsc)))
        elif lsc == 0:  # added to prevent problem where 0 is neither '+' or '-'. So a sequence: 1;2;3;4 -> Tn = n0
            return("Tn = %sn" % (lsd1))
        else:
            return("Tn = %sn+" % (lsd1) + ("%s" % (lsc)))

    elif ls2 - ls1 != ls4 - ls3:
        return("This is not a Linear Equation!")
    
    
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




