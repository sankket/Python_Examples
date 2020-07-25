#Priting the Value at Even Places 
T = (1,2,3,4,5)
print('Original Tuple elements are :',end=' ')
print(T)
l=[]
for i in T:
    #for elemnts having Remainder 0.
    if T.index(i)%2==0:
        l.append(i)
T2 = tuple(l)
print('Values at Even index are',end=' ')
print(T2)
