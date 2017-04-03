
# Linear Sequences
# Original File Moved To /Original
# ==============================================================================================================================
def tnuml(n):
    o = []
    for _ in n:
        _ = float(_)
        o.append(_)
    return o


# Way of inputing items all in one line
ls1, ls2, ls3, ls4 = tnuml(input("Enter first 4 terms... With Spaces In Between ").split())

if ls2 - ls1 == ls4 - ls3:
    lsd1 = ls2 - ls1 # common difference
    lsc = lsd1 - ls1  # constant e.g. Tn = xn + c
    lsc = lsc * -1
    # Fixes Bug
    if lsc > 0:
        lsc = "+" + str(lsc)
    if lsc == 0:  # added to prevent problem where 0 is neither '+' or '-'. So a sequence: 1;2;3;4 -> Tn = n0
        print("Tn = %sn" % (lsd1))
    else:
        print("Tn = %sn" % (lsd1) + ("%s" % (lsc)))

elif ls2 - ls1 != ls4 - ls3:
    print("This is not a Linear Equation!")


# In function form
# ======================================================================================================================
def lseq(ls1, ls2, ls3, ls4):
    if ls2 - ls1 == ls4 - ls3:
        lsd1 = ls2 - ls1  # common difference
        lsc = lsd1 - ls1  # constant e.g. Tn = xn + c
        lsc = lsc * -1
        # Fixes Bug
        if lsc > 0:
            lsc = "+" + str(lsc)
        if lsc == 0:  # added to prevent problem where 0 is neither '+' or '-'. So a sequence: 1;2;3;4 -> Tn = n0
            return ("Tn = %sn" % (lsd1))
        else:
            return ("Tn = %sn" % (lsd1) + ("%s" % (lsc)))

    elif ls2 - ls1 != ls4 - ls3:
        return ("This is not a Linear Equation!")




