L=[5,3,1,5,8,2]
x=len(L)
for i in reversed(L):
    if i<x:
        x=i
    else:
        pass
print(x)