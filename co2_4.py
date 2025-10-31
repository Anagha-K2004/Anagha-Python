#Generate a list of 4digit numbers in a given range with all their digits even and number is a perfect square
#4-digit numbers with all even digits and perfect squares:[4624, 6084, 6400,8464]

import math
for i in range(1000,10000):
    sqrtno=int(math.sqrt(i))
    if sqrtno *sqrtno == i:
        if all (int(digit)%2==0 for digit in str(i)):
                print(i)
    
