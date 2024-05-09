#!python3
"""
Create a function that calculates the amount of compound interest 
earned.
t = time in years
P = amount invested
n = # of compounding periods per year (how often interest is calculated)
Output should be rounded to 2 decimal places
r = rate of interest as a percentage
"""
def compoundInterest(p,r,t,n):
    r = r/100
    a = p*(1+r/n)**(n*t)
    a = round(a,2)
    return a
print("lord beelzebub will calculate compounding interest over a period of time.")
p = float(input("please enter the amount of money to be invested: "))
r = float(input("please enter the interest rate in percentage: "))
t = float(input("please enter an amount of time in years to be calculated: "))
n = float(input("please enter how often the interest compounds: "))
y = compoundInterest(p,r,t,n)
print(y)
assert compoundInterest(1000,4,2,4) == 1082.86
assert compoundInterest(2500,4.2,20,12) == 5782.43
assert compoundInterest(83,7,5,365) == 117.78
assert compoundInterest(10000,3,10,2) == 13468.55