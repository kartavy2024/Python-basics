def findPositiveNegetiveZero(number):
    if number == 0:
        return "zero"
    elif number <0:
        return "Negetive"
    else:
        return "Positive"
    

number = findPositiveNegetiveZero(1)
number2 = findPositiveNegetiveZero(0)
number3 = findPositiveNegetiveZero(-1)

print(f"Number 1 is {number}, Number 2 is {number2}, and Number 3 is {number3}")