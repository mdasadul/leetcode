def fun(area,numRows,numCols):
    if area[0][0]==0:
        return -1 
    
    q =[(0,0,1)]
    area[0][0] = 0
    while len(q)>0:
        x,y,d = q.pop(0)
        if area[x][y] ==9: return d 
        for(a,b) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            #print(a,b)
            if 0<=a<numRows and 0<=b<numCols and area[a][b]>=1:
                #print(a,b,area,q)
                if area[a][b]==9: return d
                area[a][b]=0 
                q.append((a,b,d+1))
                
    return -1 

a=[[1,1,1,1,1],[1,0,1,0,0],[1,1,1,9,0]]
print(fun(a,3,5))