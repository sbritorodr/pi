# Code for Basilea's problem
import time # this is used to count the time between the operations
import datetime
import math as mp
from decimal import *
def pi_basel(n):
  k = 1 # remember, should start by 1
  pi_basel = 0
  while k<n:
    pi_basel += Decimal(1/mp.pow(k,2)) #The formula
    k += 1
  pi_basel = Decimal(mp.sqrt(6 * pi_basel))
  return pi_basel

  

exact_pi_val = str(3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989)
end = 12000 # Limit range, default is 1200
start_time = time.time_ns()/1000 # start time in microseconds
for n in range(1,end): # n starts from 1. This avoids the Google Machine to be forever running.
    print(pi_basel(n))

pi_result = str(pi_basel(end))
print("\n\n" + pi_result)
computed_digits = 0
i = 0
while i < len(pi_result):
  if pi_result[i] == exact_pi_val[i]:
    computed_digits +=1
    i +=1
  else: 
    computed_digits -=1
    break
end_time = time.time_ns()/1000 # end time in microseconds
delta = datetime.timedelta(microseconds=end_time-start_time)
print("You computed " + str(computed_digits) + " digits of pi in " + str(delta), " (hours:minutes:seconds.microseconds)")