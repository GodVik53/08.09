n=int(input())
a=[randint(10,12) for i in range(n)]
print(a)
max1=1
k=1
for i in range(1,n):
    if a[i]==a[i-1]:
        k+=1
    else:
        if k>=max1:
            max1=k
        k=1
if k>max1:
    max1=k
print(max1)