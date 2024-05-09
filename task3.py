#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse rounded to 2 decimals
        None if the hypotenuse does not exist

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""
def hypotenuse(a,b):
    aa = a**2
    bb = b**2
    cc = aa + bb
    c = round(cc ** 0.5,2)
    if c > 0 and a > 0 and b > 0:
        return c
    else:
        return "None"
assert hypotenuse(6,8) == 10
assert hypotenuse(5,12) == 13
assert hypotenuse(4,6) == 7.21
assert hypotenuse(-3,4) == "None"