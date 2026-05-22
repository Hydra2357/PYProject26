# Example Python code demonstrating all major operators

# Arithmetic Operators
a = 10
b = 3
print("Arithmetic:")
print("Addition: ", a + b)          # 13
print("Subtraction: ", a - b)       # 7
print("Multiplication: ", a * b)    # 30
print("Division: ", a / b)          # 3.333...
print("Floor Division: ", a // b)   # 3
print("Modulus: ", a % b)           # 1
print("Exponentiation: ", a ** b)   # 1000

# Comparison Operators
print("\nComparison:")
print("Equal: ", a == b)            # False
print("Not Equal: ", a != b)        # True
print("Greater Than: ", a > b)      # True
print("Less Than: ", a < b)         # False
print("Greater or Equal: ", a >= b) # True
print("Less or Equal: ", a <= b)    # False

# Logical Operators
x = True
y = False
print("\nLogical:")
print("AND: ", x and y)             # False
print("OR: ", x or y)               # True
print("NOT: ", not x)               # False

# Bitwise Operators
c = 5  # Binary: 101
d = 3  # Binary: 011
print("\nBitwise:")
print("AND: ", c & d)               # 1 (001)
print("OR: ", c | d)                # 7 (111)
print("XOR: ", c ^ d)               # 6 (110)
print("NOT: ", ~c)                  # -6 (inverts bits)
print("Left Shift: ", c << 1)       # 10 (1010)
print("Right Shift: ", c >> 1)      # 2 (10)

# Assignment Operators
e = 10
print("\nAssignment:")
e += 5   # e = e + 5 -> 15
print("+= : ", e)
e -= 3   # 12
print("-= : ", e)
e *= 2   # 24
print("*= : ", e)
e /= 4   # 6.0
print("/= : ", e)
e //= 2  # 3.0
print("//= : ", e)
e %= 2   # 1.0
print("%= : ", e)
e **= 3  # 1.0
print("**= : ", e)

# Identity Operators
f = [1, 2]
g = f
h = [1, 2]
print("\nIdentity:")
print("is: ", f is g)              # True (same object)
print("is not: ", f is not h)      # True (different objects)

# Membership Operators
i = [1, 2, 3]
print("\nMembership:")
print("in: ", 2 in i)              # True
print("not in: ", 4 not in i)      # True