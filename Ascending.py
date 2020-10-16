def ascending(N):
    for i in range(0,len(N)):
        j=i+1
        for j in range(0,len(N)):
            if N[i]<N[j]:
                temp=N[i]
                N[i]=N[j]
                N[j]=temp
    print(N)

A=[10,200,30,40,50]
ascending(A)
