def perfectCity(departure, destination):
    xa = departure[0]
    xb = destination[0]
    
    ya = departure[1]
    yb = destination[1]
    
    if int(xa) == int(xb):
        hor = min(2*(int(xa)+1)-(xa + xb), (xa + xb)-2*(int(xa)))
    else:
        hor = abs(xa - xb)
        
    if int(ya) == int(yb):
        ver = min(2*(int(ya)+1)-(ya + yb), (ya + yb)-2*(int(ya)))
    else:
        ver = abs(ya - yb)
        
    return hor + ver
