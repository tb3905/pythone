def fun(x,y,n):
    arr[x-1]=y
    ans = 1
    for i in range(1,n):
        if arr[i]!=arr[i-1]:
            ans +=1
    return ("number of Stud in matrix: ",ans)
n=int(input("Number of Student:"))
k=int(input("number of revoution:"))
arr=[]
for i in range (n):
    arr.append(int(input(f"student {i+1}:")))
for i in range(k):
    x=int(input("Matrix position:"))
    y=int(input("value of revalution:"))
    print(fun(x,y,n))
