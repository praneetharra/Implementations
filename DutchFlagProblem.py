a = [1,2,1,1,3,2,3,3,1,2,1,3,3,1,2,2,2,2,2,3,1,1,2,1,3]

i = 0
j = 0
k = len(a)-1

# pull all the 1s forward
while(i<len(a)):
    if a[j] == 1 and i > j:
        j+=1
    elif a[i]==1 and i > j:
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
        j+=1
        i+=1
    else:
        i+=1

# push all 3s to the end 
i = 0
while(i<k):
    if a[k] == 3:
        k-=1
    elif a[i]==3:
        tmp2 = a[i]
        a[i] = a[k]
        a[k] = tmp2
        k-=1
        i+=1
    else:
        i+=1

print a
