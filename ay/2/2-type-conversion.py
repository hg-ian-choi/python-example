# int => str
length = len("Hello, World!")
print(type(length))
print(str(3) + str(5))

lengthString = str(length)
print(type(lengthString))


# int => float
intFloat = float(3)
print(type(intFloat))


# str => float
string = "3.1415926"
stringFloat = float(string)
print(type(stringFloat))


# test
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))
