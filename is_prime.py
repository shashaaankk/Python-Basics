def is_prime(n):
    if n>1:
        for index in range (2,n):
            if(n % index)==0:
                return "composite"
                break
        else:
            return "prime"
    elif n==1:
        return "neither prime nor composite"
    else:
        return "Enter a posotive number"

if __name__ == '__main__':
     n=int(input("Enter the number: "))
     result=is_prime(n)
     print(result)
