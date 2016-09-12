def packageBoxing(pkg, boxes):
    
    pk = pkg[:]
    back_pkg = pk[:]
    
    boxes_index = []
    pkg_vol = pk[0]*pk[1]*pk[2]
    for i in boxes:
        pk = back_pkg[:]
        a = min(i)
        if a>=min(pk):
            del i[i.index(min(i))]
            del pk[pkg.index(min(pk))]
            b = min(i)
            if b>=min(pk):
                del i[i.index(min(i))]
                del pk[pk.index(min(pk))]
                c = min(i)
                if c>=min(pk):
                    boxes_index.append(boxes.index(i))
                i.append(b)
            i.append(a)
                    
    if len(boxes_index) == 0:
        return -1
    elif len(boxes_index) > 1:
        box_vols = []
        for i in boxes_index:
            box_vols.append(boxes[i][0]*boxes[i][1]*boxes[i][2])
        return boxes_index[box_vols.index(min(box_vols))]
    else:
        return boxes_index[0]

pkg = [4, 2, 5]
boxes = [[4,3,5], 
 [5,2,5]]

packageBoxing(pkg, boxes)
