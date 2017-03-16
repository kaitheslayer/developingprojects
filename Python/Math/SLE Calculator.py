

# By: Kai Parsons
# Not designed for absolute efficiency


# Initial Start

def compute(numbers):

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
    print ("x=%s and y=%s" % (str(ans1), str(ans2)))





v1, v2, v3, v4, s1, s2 = input("Enter Matrix (a,b,c,d, x1, x2)").split()

matrix = [int(v1),int(v2),int(v3),int(v4),int(s1),int(s2)]

compute(matrix)




