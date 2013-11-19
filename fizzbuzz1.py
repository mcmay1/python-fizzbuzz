#==============================================================================
# FizzBuzz
#
# Michael Copley-May
# 19/11/13
#
# Write a program that prints numbers from 1 - 100. Replace multiples of 3 with
# 'Fizz', multiples of 5 with 'Buzz', and multiples of both 3 and 5 with
# 'FizzBuzz'.
#==============================================================================

n = 100                           # List length
N = range(n)                      # List from 0 to (n-1)

for i in N:
    N[i] += 1                     # Add 1 to each list element to get 1 to n
    fb = (N[i]/3.0,N[i]/5.0)
    N[i] = str('')                # Needs to be string to append Fizz or Buzz
    
    if fb[0] == float(int(fb[0])):
        N[i] += 'Fizz'
    if fb[1] == float(int(fb[1])):
        N[i] += 'Buzz'
    if fb[0] != float(int(fb[0])) and fb[1] != float(int(fb[1])):
        N[i] = str(i+1)

print N

#==============================================================================