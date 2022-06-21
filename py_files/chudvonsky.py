# DiclaimeR DO NOT disable the limit. Google could ban you!
import time
from datetime import timedelta
import math as mp
from decimal import *
import signal
import sys
def pi_chudn(n):
    getcontext().prec = n+50
    k=0
    pi_chud = 0
    while k<n:
        pi_chud+=(((Decimal(-1))**k ) * (Decimal(mp.factorial(6*k)))*(13591409 + 545140134*k))/Decimal((mp.factorial(3*k)*((mp.factorial(k))**3)*(640320**((3*k)+(Decimal(1.5))))))
        k+=1
    pi_chud = (Decimal(pi_chud) * 12)
    pi_chud = (Decimal(pi_chud**(-1)))
    return int(pi_chud*10**n)

def check_digits(digit_string, do_time_too = True): # this will check how many digits you've computed
    exact_pi_val = str(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989)
    pi_digits = 0
    if len(digit_string) > len(exact_pi_val):
        print("You computer more than ", len(exact_pi_val), " digits of pi!")
    else:
        for i in range(len(digit_string)): 
            if digit_string[i] == exact_pi_val[i]:
                # print("pi_val_database: ", exact_pi_val)
                pi_digits += 1
                #print("pi_digits: ", pi_digits)
        print("\nYou computed ", pi_digits, " digits of pi")
        if do_time_too:
            delta = timedelta(microseconds=end_time-start_time)
            print("\nYou computed ", pi_digits, " digits of pi in ", delta, " (hours : minutes : seconds . microseconds).")

def sigint_handler(signal, frame): # this only prints the last calculated digit when Ctrl+C
    print ('\nLast Digits calculated: \n' + pi_result)
    check_digits(pi_result, do_time_too= False)
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

end = 1200 # CHANGE THIS LIMIT
start_time = time.time_ns()/1000 # time in microseconds since epoch
for n in range(1, end): # n starts from 1. This avoids the Google Machine to be forever running.
    # print(int(exact_pi_val[:n+1]))
    if n == end:
      break
    pi_result = str(pi_chudn(n))
    print(pi_result) # COMMENT/UNCOMMENT THIS IF YOU WANT TO SEE THE PROGRESS IN THE TERMINAL
end_time = time.time_ns()/1000
print(pi_result)

check_digits(digit_string=pi_result)