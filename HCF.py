#Taking input numbers from the user
n = int(input("Input first number: "))
m = int(input("Input first number: "))

#determine smaller from the inputs
smaller = n if n > m else m                           

for num in range(1,smaller+1):                           
       if((n%num == 0) and (m%num == 0)):              # checking if the num perfectly divides both inputs
           hcf = num

print('The HCF of',n,'and',m,'is',hcf)
