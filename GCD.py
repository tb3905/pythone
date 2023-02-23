#taking inputs from the user
n = int(input("Input first number: "))
m = int(input("Input first number: "))

# Here the input values are assigned to new variables because the values change in the loop
num1 = n
num2 = m
while (num1>0 and num2>0):
        rem = num1 % num2
        num1 = num2
        num2 = rem
        
hcf = num1
print("The HCF or GCD of",n,"and",m,"is",hcf)
