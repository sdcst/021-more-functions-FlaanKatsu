#!python3
"""
Create a function that converts from degrees F to degrees C or
vice versa, depending on which initial unit is given
2 input parameters:
float: the number of degrees
string: the unit that you currently have: may be 'C' of 'F'

return: float the number of degrees of the other unit. Round answers to 2 decimals

Sample assertions:
assert convertTemp(10,'C') == 50
assert converTemp(32,'F') == 0
"""
##How to use convertTemp(): the first value is the temperature value to be converted, the second value is the current temperature type (ex. if your current units are celcius and you want to convert to F, input "C".)
def convertTemp(a,b):
    if b == "C" or b == "c":
        e = (a * 9/5) + 32
    elif b == "F" or b == "f":
        e = 5/9 * (a - 32)
    elif b != "F" or b != "f" or b != "C" or b != "c":
        e = "error: not a valid unit"
    e = round(e, 2)
    return e
TempUnit = input("Lord beelzebub will convert temperature units for you! \nPlease enter the current unit to use: (\"C\" or \"F\"): ")
TempValue = float(input("Now please enter a value: "))
end = convertTemp(TempValue, TempUnit)
if end != "error: not a valid unit" and TempUnit == "C" or TempUnit == "c":
 print(f"Lord Beelzebub has determined that {TempValue} degrees celcius is {end} degrees fahrenhiet!!")
elif end != "error: not a valid unit" and TempUnit == "F" or TempUnit == "f":
 print(f"Lord Beelzebub has determined that {TempValue} degrees fahrenhiet is {end} degrees celcius!!")
else:
 print(end)
def tests():
    assert convertTemp(10,'C') == 50.00
    assert convertTemp(32,'F') == 0.00
    assert convertTemp(100,'C') == 212.00
    assert convertTemp(100,'F') == 37.78
    
    


if __name__== "__main__":
    tests()