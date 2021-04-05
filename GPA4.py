#put this code in your main file
def date2tuple(m):
   m=m.replace(',',' ')
   dt,mt,y=m.split()
   mon={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,
            'Oct':10,'Nov':11,'Dec':12}
   mt=mt.capitalize()
   t=(int(y),mon[mt],int(dt))
   return t
