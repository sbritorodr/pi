import math as mp
import random as rnd
from decimal import *

def montecarlo(dartN = 12345, rep = 10): # number of darts to throw
    r = 1 # radius of the circle
    x = 0; y = 0 # darts coordinates
    B = 0 # number of darts inside the circle
    pi_array = [] # array to store pi values

    j = 0
    while j < rep: # will repeat the throw of N darts "rep" times
        i = 0
        while i < dartN:
            x = rnd.random() * r
            y = rnd.random() * r
            if (x**2 + y**2) <= r**2:
                B += 1
            i += 1
        j += 1
        pi_array.append(4*B/dartN) # will save the value of pi at each iteration
        B = 0 # resets the dart counter inside the circle
    pi = 0
    err = 0
    for i in range(len(pi_array)):
        pi += pi_array[i]/rep # add the mean of all values
    for i in range(len(pi_array)):
        err += (pi-pi_array[i])**2/rep # sum the error of all values
    err = mp.sqrt(err) # calculate the error

    return pi, err

pi,err = montecarlo(999, 100) # Change here the number of darts to throw and the number of repetitions

print(pi, err)