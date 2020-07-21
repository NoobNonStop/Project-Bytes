import re

def numberFinder() :
    string = input("Enter the string in which to find a phone number: ")
    regexNumber = re.compile(r"\d{10}")
    mo = regexNumber.search(string)
    print("Phone Number found: ", mo.group())
    



