# demo_all_list_methods.py
# Comprehensive example using almost every list method + important patterns

def separator(title):
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


# ────────────────────────────────────────────────
separator("1. Creating lists in different ways")

lst = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:         ", lst)

lst2 = list("python")                           # from iterable
print("From string:           ", lst2)

lst3 = [0] * 6                                  # multiplication
print("Multiplication [0]*6:  ", lst3)

lst4 = list(range(5, 15, 2))
print("From range:            ", lst4)


# ────────────────────────────────────────────────
separator("2. append()  – add one element at the end")

lst.append("fig")
print("After append('fig'):   ", lst)


# ────────────────────────────────────────────────
separator("3. extend()  – add multiple elements (better than += for iterables)")

more_fruits = ["grape", "honeydew"]
lst.extend(more_fruits)
print("After extend:          ", lst)


# ────────────────────────────────────────────────
separator("4. insert()  – insert at specific position")

lst.insert(2, "blueberry")          # insert before index 2
print("After insert(2, blueberry):", lst)


# ────────────────────────────────────────────────
separator("5. remove()  – remove first occurrence")

lst.remove("banana")
print("After remove('banana'): ", lst)


# ────────────────────────────────────────────────
separator("6. pop()  – remove & return element (by index or last)")

last = lst.pop()                    # removes and returns last
print("pop() returned:        ", last)
print("After pop():           ", lst)

second = lst.pop(1)                 # remove by index
print("pop(1) returned:       ", second)
print("After pop(1):          ", lst)


# ────────────────────────────────────────────────
separator("7. clear()  – remove all elements")

temp = lst.copy()
temp.clear()
print("After clear():         ", temp)


# ────────────────────────────────────────────────
separator("8. index()  – find first position of value")

pos = lst.index("cherry")
print("index('cherry') →     ", pos)

# pos = lst.index("kiwi")           # ValueError if not found


# ────────────────────────────────────────────────
separator("9. count()  – how many times value appears")

fruits = ["kiwi", "apple", "kiwi", "mango", "kiwi", "apple"]
print("List:                  ", fruits)
print("count('kiwi') →       ", fruits.count("kiwi"))
print("count('apple') →      ", fruits.count("apple"))


# ────────────────────────────────────────────────
separator("10. sort()  – in-place sorting")

numbers = [65, 12, 99, 3, 45, 78, 21]
print("Before sort:           ", numbers)

numbers.sort()
print("After sort():          ", numbers)

numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)


# ────────────────────────────────────────────────
separator("11. reverse()  – reverse list in place")

colors = ["red", "green", "blue", "yellow"]
print("Before reverse:        ", colors)
colors.reverse()
print("After reverse():       ", colors)


# ────────────────────────────────────────────────
separator("12. copy()  – shallow copy (very important!)")

a = [1, 2, [10,20], 4]
b = a.copy()               # recommended way
c = a[:]                   # also common
d = list(a)                # another way

print("Original a:            ", a)
print("copy() b:              ", b)

# Demonstrate why copy matters
a[2][0] = 999              # nested list → shallow copy problem
print("\nAfter a[2][0] = 999")
print("a →                    ", a)
print("b (copy) →             ", b)     # also changed! (shallow)
print("But integers are fine: ", a[0], b[0])


# ────────────────────────────────────────────────
separator("Bonus: Common patterns & tricks 2025 style")

# List comprehension examples
squares = [x*x for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
print("squares:               ", squares[:6], "...")
print("evens:                 ", evens)

# zip + list comprehension (very common)
names = ["raj", "priya", "amit"]
ages  = [25, 32, 19]
people = [f"{n} ({a})" for n, a in zip(names, ages)]
print("zipped list comp:      ", people)

# sorted() → returns NEW list (vs sort() in-place)
unsorted = [42, 7, 19, 88, 3]
sorted_version = sorted(unsorted)
print("sorted() result:       ", sorted_version)
print("original unchanged:    ", unsorted)


print("\n" + "─"*70)
print("End of list methods demo")
print("Most used in real code: append, extend, pop, sort, copy, list comp")