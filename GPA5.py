def oddeven(lst):
    counteven=0
    countodd=0
    mst=[]
  
    j=0
    m=1
    for i in lst:
        if i%2 !=0:
            j=j+i
            countodd+=1
        else:
            counteven+=1
            m=m*i
            
    mst.append(j)     
    mst.append(m)
    return tuple(mst)
# changes in main.py
# ans = oddeven([1,2,3,4,5])  put this line in place of  ans = oddeven("29 Jul, 2009")
