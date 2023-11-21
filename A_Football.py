num = input()
count=1
i=1
while count<7 and i < len(num):
    if num[i-1]==num[i]:
        count+=1
    else:
        count=1
    i+=1
if count>=7:
    print("YES")
else:
    print("NO")