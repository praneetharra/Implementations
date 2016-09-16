def catalogUpdate(catalog, updates):
    
    cats = [catalog[i][0] for i in range(len(catalog))]
    
    updt = [updates[i][0] for i in range(len(updates))]
    
    for c in updt:
        if c in cats:
            i = cats.index(c)
            j = updt.index(c)
            
            for k in range(1,len(updates[j])):
                catalog[i].append(updates[j][k])
            temp = catalog[i][1:]
            temp.sort()
            del catalog[i][1:]
            catalog[i] = catalog[i]+temp
            updt[j] = ''
                
        else:
            i = updt.index(c)
            catalog.append(updates[i])
            cats.append(c)
            updt[i] = ''
            
    catalog.sort()
    return catalog



#Input
catalog = [["Books","Classics","Fiction "], 
 ["Electronics","Cell Phones","Computers","Ultimate item"], 
 ["Grocery","Beverages","Snacks"], 
 ["Snacks","Chocolate","Sweets"], 
 ["root","Books","Electronics","Grocery"]]
           
updates = [["Snacks","Marmalade"], 
 ["Fiction ","The Chronicles of Narnia"], 
 ["Fiction ","Fiction stories"], 
 ["Snacks","Tuc"], 
 ["root","T-shirts-men"], 
 ["T-shirts-men","My little pony t-shirt"], 
 ["Fiction ","Harry Potter"], 
 ["root","T-shirts"], 
 ["T-shirts","CodeFights"], 
 ["Fiction stories","Frozen heart"], 
 ["Fiction stories","Marvel films"], 
 ["Marvel films","Ant-man"], 
 ["Marvel films","Avengers"]]
           
catalogUpdate(catalog, updates)
