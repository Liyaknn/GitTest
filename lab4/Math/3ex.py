import math

def area_of_regular_polygon(sides, length):
 
  apothem = length / (2 * math.tan(math.pi / sides))

 
  area = int(0.5 * sides * length * apothem)

  return area



sides = int(input("The number of sides: "))
length = int(input("The side length: "))

area = area_of_regular_polygon(sides, length)


print("The area of the polygon is:", area)