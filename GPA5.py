def oddeven(lst):
    counteven=0
    countodd=0
    mst=[]
  
    j=0
    m=1
    for i in lst:
        if i%2 !=0:
            j=j+i
            countodd=+1
        else:
            counteven=+1
            m=m*i
            
    mst.append(j)     
    mst.append(m)
    return tuple(mst)
