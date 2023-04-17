# Name:Jiwoong Jung
# SBUID: 115943061
##################### SCORE ######################
####### Score:  8/10
#################################################
# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit):
    return (fahrenheit-32.0) * (5.0/9.0)


def what_to_wear(celsius):
    if celsius < -10:
        print("Wear puffy jacket!")
    elif celsius == -10:
        print("Wear puffy jacket or scarf!")
    elif -10 < celsius < 0:
        print("Wear scarf!")
    elif celsius == 0:
        print("Wear scarf or sweater!")
    elif 0 < celsius < 10:
        print("Wear sweater!")
    elif celsius == 10:
        print("Wear sweater or light jacket!")
    elif 10 < celsius < 20:
        print("Wear light jacket!")
    elif celsius == 20:
        print("Wear light jacket or T-shirt!")
    elif 20 < celsius:
        print("Wear T-shirt!")



# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):   # The area of the triangle is : 6.0 , its perimeter is : 12.0 is wrong.. check for the logic and parenthesis in python. Also use variables and functions --> -4
    return abs((((x1*y2) + (x2*y3) + (x3*y1)) - ((x1*y3) + (x2*y1) + (x3*y2)))/2)

def euclidean_distance(x1, y1, x2, y2):
    return (((x1-x2)**2)+((y1-y2)**2))**0.5

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    return ((((x1-x2)**2)+((y1-y2)**2))**0.5) + ((((x2-x3)**2)+((y2-y3)**2))**0.5) + ((((x3-x1)**2)+((y3-y1)**2))**0.5)


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    return deg*((math.pi)/180)

def apothem(number_sides, length_side):
    return length_side / (2*math.tan(deg2rad(180/number_sides)))

def polygon_area(number_sides, length_side):
    return (number_sides * length_side * (length_side / (2*math.tan(deg2rad(180/number_sides)))))/2


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
print(fahrenheit2celsius(fahrenheit))
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = 4, 0, 4, 3, 0, 0 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

