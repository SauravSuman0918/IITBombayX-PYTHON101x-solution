# Write a Function called word_freq which takes one string argument
# Perform a count of the number of 'n' character words in this string and return a list of tuples
# Define your function called `word_freq` below
def word_freq(sentence):
    lst=[]
    mst=sentence.split(' ')
    for i in mst:
        m=len(i)
        lst.append(m)
    lst.sort(reverse=True)
    count6=0
    count5=0
    count4=0
    count3=0
    count2=0
    count1=0
    
    
    psu=[]
    for i in lst:
        if i==6:
            count6+=1
        if i==5:
            count5+=1
        if i==4:
            count4+=1
        if i==3:
            count3+=1
        if i==2:
            count2+=1
        if i==1:
            count1+=1
    if count6!=0:
        t=(6,count6)
        psu.append(t)
   
    if count5!=0:
        t=(5,count5)
        psu.append(t)
        
   
    if count4!=0:
        t=(4,count4)
        psu.append(t)
    
    if count3!=0:
        t=(3,count3)
        psu.append(t)
   
    if count2!=0:
        t=(2,count2)
        psu.append(t)
    
    if count1!=0:
        t=(1,count1)
        psu.append(t)
    
    return psu
