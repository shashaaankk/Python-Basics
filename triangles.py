#Right Triangle left weighted
def right_triangle_left_weighted(n):
    print("\n")
    for i in range (1,n+1):
        print('*'*i)
    print('___________________________')

#Right Triangle Right weighted
def right_triangle_right_weighted(n):
    print("\n")
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)
    print('___________________________')

#Equilateral Triangle
def equilateral_triangle(n):
    print("\n")
    for i in range(1,n+1):
        print(" "*(n-i)+"* "*i)


#Right Triangle left weighted and reversed
def right_triangle_left_weighted_rev(n):
    print("\n")
    for i in reversed(range(1,n+1)):
        print('*'*i)
    print('___________________________')

#Right Triangle Right weighted
def right_triangle_right_weighted_rev(n):
    print("\n")
    for i in reversed(range(1,n+1)):
        print(" "*(n-i)+"*"*i)
    print('___________________________')


#Reversed Equilateral Triangle
def reversed_equi_triangle(n):
    for i in reversed(range(1,n+1)):
        print(" "*(n-i)+"* "*i)
    print('___________________________')

def diamond(n):
    print("\n")
    for i in (range(1,n+1)):
        print(" "*(n-i)+"* "*i)
    for i in (range(n-1,0,-1)):
        print(" "*(n-i)+"* "*i)



ip=int(input("Enter the number of rows: "))
right_triangle_left_weighted(ip)
right_triangle_right_weighted(ip)
equilateral_triangle(ip)
right_triangle_left_weighted_rev(ip)
reversed_equi_triangle(ip)
right_triangle_right_weighted_rev(ip)
diamond(ip)
