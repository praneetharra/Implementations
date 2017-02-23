def parkingSpot(carDimensions, parkingLot, luckySpot):
    result = True
    
    length = carDimensions[0]
    width = carDimensions[1]
    lx = luckySpot[0]
    ly = luckySpot[1]
    rx = luckySpot[2]
    ry = luckySpot[3] 
    
    if abs(lx-rx)+1 != width and abs(ly-ry)+1 != width:
        return False
# if car fits vertically    
    if abs(lx-rx)+1 == width:
# if fits from top
        for i in range(lx,rx+1):
            for j in range(ry+1):
                if parkingLot[i][j] == 1:
                    result = False
        if result == True:
            return True
# if fits from bottom
        else:
            result = True
            for i in range(lx,rx+1):
                for j in range(ly,len(parkingLot[0])):
                    if parkingLot[i][j] == 1:
                        result = False
            if result == True:
                return True
            else:
                return False
#if car fits horizontally
    else:
#if car fits from left
        for i in range(rx+1):
            for j in range(ly,ry+1):
                if parkingLot[i][j] == 1:
                    result = False
        if result == True:
            return True
        else:
#if car fits from right
            result = True
            for i in range(lx, len(parkingLot)):
                for j in range(ly,ry+1):
                    if parkingLot[i][j] == 1:
                        result = False
            if result == True:
                return True
            else:
                return False
            

carDimensions = [2,1]
parkingLot = [[1,1,1,1], 
 [1,0,0,0], 
 [1,0,1,0]]
luckySpot = [1, 2, 1, 3]

parkingSpot(carDimensions, parkingLot, luckySpot)
