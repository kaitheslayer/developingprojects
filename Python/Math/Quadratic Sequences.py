# quadractic sequences

def tnuml(n):
    o = []
    for _ in n:
        _ = float(_)
        o.append(_)
    return o

#============================================================
# Fixed numbers operate as floats no need to call int()
# Need to fix when = 0 doesnt show
#============================================================

qs1, qs2, qs3, qs4 = tnuml(input("Enter first 4 terms... With Spaces In Between ").split())
# e.g.  9    16   25   36

# split the if statement below into variables: it works
d1=qs3-qs2
d2=qs2-qs1
d3=qs4-qs3
d4=qs3-qs2
d5=d1-d2

    # checking if 2nd difference is constant
if d1-d2==d3-d4:
    a=d5/2 # a = 2nd difference/2
    b=qs2-qs1-3*a # b = (T2 - T1)-3a
    c=qs1-a-b # c = T1-(a+b)
    print("Tn = %sn² + %sn + %s" % (a, b, c))  # need to fix output so not float if not
    # use your factor genorator to add (x+y)(x+y) format

else:  # this line no longer works: enter: 1; 2; 3; 4
    print("This is not a quadratic sequence!")
    
    
# In Function Form
    
def qseq (qs1, qs2, qs3, qs4):
    d1 = qs3 - qs2
    d2 = qs2 - qs1
    d3 = qs4 - qs3
    d4 = qs3 - qs2
    d5 = d1 - d2

    # checking if 2nd difference is constant
    if d1 - d2 == d3 - d4:
        a = d5 / 2  # a = 2nd difference/2
        b = qs2 - qs1 - 3 * a  # b = (T2 - T1)-3a
        c = qs1 - a - b  # c = T1-(a+b)
        return "Tn = %sn² + %sn + %s" % ( a, b, c)
        # use your factor genorator to add (x+y)(x+y) format

    else:  # this line no longer works: enter: 1; 2; 3; 4
       return "This is not a quadratic sequence!"

# EG
print (qseq(9,16,25,36))
