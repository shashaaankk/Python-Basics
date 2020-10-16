def is_palindrome(str):
    check_str=str[::-1]
    if check_str==str:
        return "PALINDROME"
    return "NOT PALINDROME"


ip=input("Enter NUMBER/STRING: ")
print(is_palindrome(ip))
