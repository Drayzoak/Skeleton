class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Booltile():
    def __init__(self,X,Y,bool):
        self.tilelist = []
        grid = []
        
        for y in range(Y):
            row = []    
            for x in range(X):
                row.append(bool)
            grid.append(row)
        
        self.booltilegrid = grid
        self.length = tuple((X,Y))
        
    def setbool(self,x,y,bool):
        if self.booltilegrid[x][y] == bool:
            return 
        else:
            self.booltilegrid[x][y] = bool;
            if bool == True:
                self.tilelist.append(tuple(x,y))
            else:
                self.tilelist.remove(tuple((x,y)))
            return
    
    def getbool(self,x,y):
        return self.booltilegrid[x][y]
 
    def show(self):
        for y in self.booltilegrid:
            print(y)
            print("2")
        