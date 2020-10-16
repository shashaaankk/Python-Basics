N=[1000,630,20,340,50,600,70,800,9,108]
length=len(N)
half=int(length/2)
N.sort()
#print(N)
first_half=[]
second_half=[]
for count in range(half):
    first_half.append(N[count])
for count in range(half,length):
    second_half.append(N[count])
second_half.sort(reverse=True)
for count in range(half):
    first_half.append(second_half[count])
print(first_half)
