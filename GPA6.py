#put this code in answer.py
def createlist(n):
    lst=[]
    for i in range(1,n,2):
        lst.append(i*i)
    return lst
