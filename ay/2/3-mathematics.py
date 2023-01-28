############ mathematics ############
# Rule: PEMDAS
#   Parentheses               => ()
#   Exponentiation            => **
#   Multiplication / Division => * / /
#   Addition / Subtraction    => + / -
addition = 3 + 5  # 8
print(addition)  # int

subtraction = 7 - 3  # 4
print(subtraction)  # int

multiplication = 3 * 2  # 6
print(multiplication)  # int

division = 6 / 3  # 2.0
print(division)  # float

exponentiation = 2**3  # == (2 * 2 *2) = 8
print(exponentiation)  # int

# Floor division
floorDivision = 7 // 3  # 7 / 3 = 2...1 => 2
print(7 // 3)  # int

# Modulus
remainder = 7 % 3  # 7 / 3 = 2...1 => 1
print(7 % 3)  # int

# round()
print(7 / 3)  # 2.3333333333333335
print(round(7 / 3))  # == 2 + 0.3333333333333335 >= 0.5 ? 1 : 0 = 3
