'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
Sample Input
9
10 20 20 10 10 30 50 10 20
Sample Output
3
'''
import math
def sockMerchant(n, ar):
    count=0
    pairs=0
    key=[]
    for i in range(n):
        ref=ar[i]
        if ref not in key:
           key.append(ref)
        else:
            continue
        count=1
        for j in range(i+1,n):
            if ar[j]==ref:
                count+=1
        x=math.floor(count/2)
        pairs+=int(x)
    return pairs

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
