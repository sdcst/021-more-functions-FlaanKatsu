#!python3

"""
Create a function that determines the area of a circle if given the radius
1 input parameter
float: radius

return: float area for the circle

note: Area of a circle is given by A = pi*(square of the radius)
You may want to use the math module to complete this problem
"""
#create functions
def area(r):
    a = 3.14159265359 * (r ** 2)
    return a
def getInput():
    s = input("Please enter the radius of a circle, will calculate it's area: ")
    try:
        s = float(s)
    except:
        s = "error"
    return s
#mainline code
e = area(getInput())
print(f"The area of your cirle is {e}.")
#test
assert round(area(2),2) == 12.57