n=int(input())
for i in range(2,n):
    if(n%i==0):
        print("Not prime")
        break
    else:
        print("its prime")
        break
