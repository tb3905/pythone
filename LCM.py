#Taking inputs from the user
n = int(input("Input first number: "))
m = int(input("Input first number: "))

#finding greater number from the inputs
greater_num = n if n > m else m

while(True):
       if(greater_num % n == 0 and greater_num % m == 0):         # condition for a number to be LCM to two numbers.
           lcm = greater_num
           break
       greater_num += 1

print('The LCM of',n,'and',m,'is',lcm)
