def find(l,h,a,e):
    if l==h:
        if a[h] == e:
            return h
        else:
            return None
    else:
        if e == a[int((l+h)/2)]:
            return int((l+h)/2)
            
        elif e<a[int((l+h)/2)] and e<=a[l]:
            return find(int((l+h)/2),h,a,e)

        	
        elif e<a[int((l+h)/2)] and e>a[l]:
            return find(l,int((l+h)/2),a,e)
            
        elif e>a[int((l+h)/2)] and e>a[h]:
            return find(l,int((l+h)/2,a,e))
            
        elif e>a[int((l+h)/2)] and e<=a[h]:
            return find(int((l+h)/2),h,a,e)

            
arr = [32,36,37,39,45,47,53,54,57,62,62,1,3,4,5]
element = 3
print(find(0,len(a)-1,arr,element))
