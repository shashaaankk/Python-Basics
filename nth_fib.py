def nfibb(n):
    if n<=0:
        return "INVALID INPUT"
    else:
        if n==1:
            return 0
        elif n==2:
            return 1
        else:
            return nfibb(n-1)+nfibb(n-2)

print(nfibb(4))
