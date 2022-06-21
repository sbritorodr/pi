import math as mp
from decimal import *

def ngonpi(n):
    # What now follows is to increase the number of sides from an inscribed square and a circumscribed octagon.
    r = 1 # radius of the circumference
    polA = Decimal(4 * mp.sqrt(2) * r) # perimeter of a square inside the circumference
    polB = Decimal(8 * r) # perimeter of an octagon (twice the sides of the square) outside the circumference

    m = 4 # side number

    while m*2 <= n:
        polB = Decimal(2 * polA * polB / (polA + polB))
        polA = Decimal(mp.sqrt(polA * polB))
        m = m * 2 # double increment
    pi = Decimal((polA / 2 / r + polB / 2 / r) /2) # mean of the perimeter of both polygons
    err = abs(polA / 2 / r - polB / 2 / r) /2 # the subtraction of the perimeter gives us the error
    return pi, err

def check_digits(digit_string): # this will check how many digits you've computed
    exact_pi_val = str(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989)
    pi_digits = 0
    if len(digit_string) > len(exact_pi_val):
        print("You've computed more digits than the database!")
    else:
        for i in range(len(digit_string)): 
            if digit_string[i] == exact_pi_val[i]:
                # print("pi_val_database: ", exact_pi_val)
                pi_digits += 1
                #print("pi_digits: ", pi_digits)
        print("\nYou computed ",pi_digits," digits of pi!")

n = 12345678 # maximum sides of the polygon, change this to change pi accuracy
pi, err = ngonpi(n)
print(pi)
check_digits(digit_string = str(pi))