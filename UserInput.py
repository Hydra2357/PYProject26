import sys
import argparse
import getpass

# Method 1: input() for console input
print("Method 1: Using input()")
name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
except ValueError:
    age = 0  # Default on error
print(f"Hello, {name}! You are {age} years old.\n")

# # Method 2: sys.stdin for streamed input
# print("Method 2: Using sys.stdin (enter lines, end with Ctrl+D/Z)")
# stream_data = sys.stdin.read().strip()
# print(f"Streamed data: {stream_data}\n")

# Method 3: sys.argv for command-line args
print("Method 3: Using sys.argv")
if len(sys.argv) > 1:
    cli_name = sys.argv[1]
    print(f"CLI name: {cli_name}")
else:
    print("No CLI args provided.\n")

# Method 4: argparse for advanced CLI parsing
print("Method 4: Using argparse")
parser = argparse.ArgumentParser(description="Input Demo")
parser.add_argument("cli_name", nargs='?', help="Your name (positional)", default="Unknown")
parser.add_argument("--cli_age", type=int, help="Your age (optional)", default=0)
args = parser.parse_args()
print(f"Parsed name: {args.cli_name}, Age: {args.cli_age}\n")

# Method 5: getpass for secure input
print("Method 5: Using getpass")
password = getpass.getpass("Enter password (hidden): ")
print("Password entered securely.\n")

# Method 6: File input (assuming 'input.txt' exists or was redirected)
print("Method 6: Reading from file (if redirected or file exists)")
try:
    with open('input.txt', 'r') as file:
        file_data = file.read().strip()
    print(f"File data: {file_data}")
except FileNotFoundError:
    print("No input file found.")

# # age = input("How old are u?")
# h1 = int(input("How tall are u?"))
# print("Your height is",h1)
#
# name = input("Enter the name: ").strip()
# age = int(input("Enter the age: ").strip())
#
# while True:
#     try:
#         age = int(input("Enter the age: "))
#         if age < 0 or age > 150:
#             print("Please enter the realistic age..")
#             continue
#         break
#     except ValueError:
#         print("This is not A valid number. Try again..")
#
# print(f"Your are{age} years old.")
#
# # Single line → single number
# n = int(input())
#
# # Single line → two numbers
# a, b = map(int, input().split())
#
# # Single line → many numbers → list
# arr = list(map(int, input().split()))
#
# # String (remove extra spaces)
# name = input().strip()
#
# # Many test cases – classic beginner style
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))