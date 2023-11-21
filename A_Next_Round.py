import sys

def invr():
    return(map(int,input().split()))
    
n,k=map(int,input().split())
s=map(int,input().split())
scores=list(s)
# inp()
# score=inp()
# lst=inlt()
count=0
for i in range(0,n):
    if scores[i] >= scores[k-1] and scores[i]>0:
        count+=1
    else: 
        break
print(count)