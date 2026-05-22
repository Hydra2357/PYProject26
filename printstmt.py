# ================================
# COMPLETE GUIDE TO print() IN ONE CODE
# ================================

import sys
import time
import pprint

# -------------------------------
# 1. Basic Printing
# -------------------------------
print("Hello World")                 # Printing a string
print(10)                            # Printing integer
print(3.14)                          # Printing float
print(True)                          # Printing boolean

# -------------------------------
# 2. Printing Multiple Values
# -------------------------------
print("Age:", 21)                    # Default separator is space

# -------------------------------
# 3. Using sep Parameter
# -------------------------------
print("Python", "Java", "C++")       # Default separator (space)
print("Python", "Java", "C++", sep=" | ")  # Custom separator

# -------------------------------
# 4. Using end Parameter
# -------------------------------
print("Hello", end=" ")              # Ends with space instead of newline
print("World")                       # Continues on same line

print("Line1", end="---")            # Custom ending
print("Line2")

# -------------------------------
# 5. Escape Characters
# -------------------------------
print("Hello\nWorld")                # New line
print("Name:\tHydra404")             # Tab space
print("This is a backslash: \\")     # Backslash
print("He said \"Python is easy\"")  # Double quote inside string

# -------------------------------
# 6. String Formatting
# -------------------------------

name = "Hydra404"
age = 20
pi = 3.14159

# Old style formatting
print("Name: %s Age: %d" % (name, age))

# format() method
print("Name: {} Age: {}".format(name, age))

# f-string (recommended)
print(f"Name: {name} Age: {age}")
print(f"5 + 5 = {5+5}")              # Expression inside f-string
print(f"Pi rounded: {pi:.2f}")       # Decimal formatting

# -------------------------------
# 7. Printing Data Types
# -------------------------------
print(type(10))
print(type(3.14))
print(type("Python"))
print(type([1, 2, 3]))

# -------------------------------
# 8. Printing Collections
# -------------------------------
lst = [1, 2, 3]
print(lst)

d = {"name": "Hydra404", "age": 20}
print(d)

# Pretty printing dictionary
pprint.pprint(d)

# -------------------------------
# 9. Printing Without Spaces
# -------------------------------
print("A", "B", "C", sep="")         # No separator

# -------------------------------
# 10. Printing to a File
# -------------------------------
with open("output.txt", "w") as f:
    print("Hello File", file=f)      # Output written to file

# -------------------------------
# 11. Using flush=True
# -------------------------------
for i in range(3):
    print(i, flush=True)             # Forces immediate output
    time.sleep(0.5)

# -------------------------------
# 12. Pattern Printing
# -------------------------------
for i in range(5):
    print("*" * i)                   # Triangle pattern

# -------------------------------
# 13. Text Alignment
# -------------------------------
print(f"{'Name':<10}{'Age':>5}")     # Left and right alignment
print(f"{'Hydra404':<10}{20:>5}")

# -------------------------------
# 14. Number Formatting
# -------------------------------
num = 1234567
print(f"{num:,}")                    # Comma separator
print(f"{num:.2f}")                  # Decimal format

# -------------------------------
# 15. Internals Example
# -------------------------------
print("This goes to stdout", file=sys.stdout)

# ====== DECLARATIONS ======

print("\n\nNumeric Types")
a = 10                # int
b = 10.5              # float
c = 3 + 4j            # complex

# Boolean
d = True

# String
e = "Hello Python"

# Sequence Types
f = [1, 2, 3]         # list
g = (1, 2, 3)         # tuple
h = range(5)          # range

# Set Types
i = {1, 2, 3}         # set
j = frozenset({4, 5, 6})  # frozenset

# Mapping
k = {"name": "John", "age": 25}   # dict

# Binary Types
l = b"hello"          # bytes
m = bytearray(5)      # bytearray
n = memoryview(bytes(5))  # memoryview

# None Type
o = None


# ====== PRINT TYPES BELOW ======

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))

# Example
print(type(10))