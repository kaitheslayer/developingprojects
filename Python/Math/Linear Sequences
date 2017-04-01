
# Original Scroll down for v2
print("Enter the first four terms of the sequence")

# works with given variables, does not work with inputs(hence the comments below which you can remove the '#'s to work with)
ls1=3    #ls1 = input("Term 1: ")
ls2=5    #ls2 = input("Term 2: ")
ls3=7    #ls3 = input("Term 3: ")
ls4=9    #ls4 = input("Term 4: ")


if ls2-ls1 == ls4-ls3:
    lsd1=ls2-ls1 #common difference
    lsc=lsd1-ls1 #constant e.g. Tn = xn + c
    if lsd1 == 1:   # added to change Tn = 1n to Tn = n
        print("Tn = n")
    elif lsc==0:  # added to prevent problem where 0 is neither '+' or '-'. So a sequence: 1;2;3;4 -> Tn = n0
       print("Tn = %sn"%(lsd1))
    else:
        print("Tn = %sn"%(lsd1)+("%s"%(lsc)))

elif ls2-ls1!=ls4-ls3:
    print("This is not a Linear Equation!")
    
    
    
    
    # Linear Sequences Improved

print("Enter the first four terms of the sequence")

# works with given variables, does not work with inputs(hence the comments below which you can remove the '#'s to work with)
    # Fix by using int() on each variable

# Way of inputing items all in one line
ls1, ls2, ls3, ls4 = input("Enter first 4 terms... With Spaces In Between ").split()

# Original bug: Always outputed xn - y not xn + y
# Current bug if Tn = xn-y prints xn +-y, We should add a function to auto correct this...
# Removed 1n to n if statement

if int(ls2)-int(ls1) == int(ls4)-int(ls3):
    lsd1=int(ls2)-int(ls1) #common difference
    lsc=int(lsd1)-int(ls1) #constant e.g. Tn = xn + c
    lsc= int(lsc) * -1
    # Fixes Bug
    if lsc > 0:
        lsc = "+" + str(lsc)
    if lsc==0:  # added to prevent problem where 0 is neither '+' or '-'. So a sequence: 1;2;3;4 -> Tn = n0
       print("Tn = %sn"%(lsd1))
    else:
       print("Tn = %sn"%(lsd1)+("%s"%(lsc)))

elif int(ls2)-int(ls1)!=int(ls4)-int(ls3):
    print("This is not a Linear Equation!")


# ======================================================================================================================

# In function form
def lseq(ls1, ls2, ls3, ls4):
    if int(ls2) - int(ls1) == int(ls4) - int(ls3):
        lsd1 = int(ls2) - int(ls1)  # common difference
        lsc = int(lsd1) - int(ls1)  # constant e.g. Tn = xn + c
        lsc = int(lsc) * -1
        if lsc > 0:
            lsc = "+" + str(lsc)
        if lsc == 0:  # added to prevent problem where 0 is neither '+' or '-'. So a sequence: 1;2;3;4 -> Tn = n0
            return ("Tn = %sn" % (lsd1))
        else:
            return ("Tn = %sn" % (lsd1) + ("%s" % (lsc)))

    elif int(ls2)-int(ls1)!=int(ls4)-int(ls3):
        return ("This is not a Linear Equation!")


# Example use
print(lseq(68, 132, 196, 260))
