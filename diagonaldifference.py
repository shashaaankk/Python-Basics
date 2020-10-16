'''abs diagonal differnce'''
def diagonalDifference(arr):
    col=len(arr)-1
    row=0
    ppl_diag=0
    rev_diag=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                ppl_diag+=arr[i][j]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j==col and i==row:
               rev_diag+=arr[i][j]
               col-=1
               row+=1
    return abs(ppl_diag-rev_diag)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
