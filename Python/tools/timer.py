# Timer Functions

def tstart():
    var = datetime.datetime.now()
    return var


def tend(i):
    o = datetime.datetime.now() - i
    return o



# Example
import datetime

timer1 = tstart()

a = 14 ** 7543
print(a)

timerend = tend(timer1)

print(" I took : " + str(timerend))




