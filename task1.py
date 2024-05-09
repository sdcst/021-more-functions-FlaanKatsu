#!python3
"""
Create a function that converts the price of Bitcoin into Canadian Dollars .
The function will require 2 input parameters:
float: amount of currency being converted

return: float value in Canadian Dollars
You will make use of a local variable called "currBTC"
currBTC shows that the conversion is 1 btc = 86,669 cad (May 7th, 1:00 PM (UTC -8), 2024)

Note: i updated the BTC conversion rate with current values. Respectively, i have patched the assert script to match the changes.

Sample assertions:

assert btcTocad(1) == 86,669
(2 points) 
"""
currBTC = 86669

b = (input("Please enter a value in BTC to convert to CAD."))
try:
 b = float(b)
 b = round(b,8) ##the equvalent of a cent in BTC is called "サトシ(satoshi)" based on the supposed name of the creator of bitcoin, which goes up to 8 decimal places.
except:
 b = "error"
def btcTocad(n):
    try:
        n = n/5
        n = n*5
        a = n * currBTC
        return a
    except:
        return("error")
if b != "error":
 c = btcTocad(b)
 round(c, 2)
 print(f"{b} in BTC is ${c} in CAD.")
elif b == "error":
 print("error: not a valid number")

"""
This checks to see if you are running the program as the main script or
if it is imported by another program.
If this py file is imported by another program, then the commands below
are not executed.
"""
if __name__ == "__main__":
    assert btcTocad(1) == 86669
    assert btcTocad(2.5) == 216672.5
    assert btcTocad("one") == "error"
