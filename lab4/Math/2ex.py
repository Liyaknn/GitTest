import math
def the_area_of_a_trapezoid(h,a,b):

    s=(a+b)/2*h
    return s

h=int(input("height:"))
a=int(input("Base, first value:"))
b=int(input("Base, second value:"))


s=the_area_of_a_trapezoid(h,a,b)

print("The area of a trapezoid", s)
