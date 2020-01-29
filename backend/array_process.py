import numpy as np
#For attendance 3 sec grace only, not for

a=np.array([1,1,0,0,1,0])
# print(len(a))
n=len(a)
print(a[n-1])
m=n%3
if(m==1):
    ad=2
if(m==2):
    ad=1
if(m==0):
    ad=0

while ad!=0:
    a=np.append(a,a[n-1])
    ad=ad-1

print(a)
nl=len(a)
ind=0
na=[]
while ind!=nl:
    n1=a[ind]*0.5
    n2=a[ind+1]*0.5
    n3=a[ind+2]*0.5
    nn=n1+n2+n3
    na.append(nn)
    ind=ind+3

count0=0
count1=0
j=0
while j<len(na):
    if(na[j]<=0.5):
        na[j]=0
        count0=count0+1
    if(na[j]>0.5):
        na[j]=1
        count1=count1+1
    j=j+1

print(na)
print("no of 0's",count0)
print("no of 1's",count1)