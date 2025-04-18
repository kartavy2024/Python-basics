def oddEven(Number):
    if Number % 2 ==0:
        return "Even"
    else:
        return "Odd"
    
find = oddEven(11)
find2 = oddEven(12)

print(f"The 11 is {find} and 12 is {find2}")