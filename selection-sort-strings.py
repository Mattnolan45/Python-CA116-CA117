a=[]
line=raw_input()

while line!="end":
   a.append(line)
   line=raw_input()


i=0
while i<len(a)-1:
   p=i
   j=i+1
   while j<len(a):
      if a[j] < a[p]:
         p=j
      j+=1
    
   tmp= a[p]
   a[p]=a[i]
   a[i]=tmp
   
   i+=1 

j=0
while j<len(a):
   print a[j]
   j+=1
