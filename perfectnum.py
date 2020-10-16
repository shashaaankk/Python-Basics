def perfect_num(n):
    divisor=0
    for i in range(1,n):
        if(n % i)==0:
            divisor+=i
            continue
    if divisor==n:
        return "Perfect Number"
    return "Not a Perfect Number"

if __name__ == '__main__':
    n=int(input("Enter number: "))
    print(perfect_num(n))
