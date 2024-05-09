#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(a,b,c):
    t = [a,b,c]
    t.sort()
    if t[2] >= (t[1] + t[0]):
        return 0
    else:
        aa = t[0] ** 2
        bb = t[1] ** 2
        cc = t[2] ** 2
        if aa + bb < cc:
            return 3
        elif aa + bb == cc:
            return 2
        elif aa + bb > cc:
            return 1

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
