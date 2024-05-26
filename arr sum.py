arr=[]
n=int(input())
for i in range (n):
    arr.append(int(input(f"Enter num {i+1}:")))
a=0
for i in range (n):
    a=a+arr[i]
    if a==0:
        for j in range (0,i+1):
            print(arr[j])
        print("code")
