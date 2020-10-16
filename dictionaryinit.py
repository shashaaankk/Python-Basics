alist=["1","2,","3","4","5","3","3","2","1"]
count=dict()
for num in alist:
    if num not in count:
        count[num]=1
    else:
        count[num]+=1
x=list(dict.fromkeys(alist))
print(x)
