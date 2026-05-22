# =====================================================
# SINGLE SCRIPT: All Common Python Exceptions Demo
# Python 3.12+ 
# Run this file to see all exceptions in action
# =====================================================

import sys

print("=== Python Exception Handling Demo ===\n")

def demo_exceptions(undefined_variable=None):
    exceptions_demo = []

    # 1. ZeroDivisionError
    try:
        10 / 0
    except ZeroDivisionError as e:
        exceptions_demo.append(f"1. ZeroDivisionError: {e}")

    # 2. ValueError
    try:
        int("abc")
    except ValueError as e:
        exceptions_demo.append(f"2. ValueError: {e}")

    # 3. TypeError
    try:
        "2" + 3
    except TypeError as e:
        exceptions_demo.append(f"3. TypeError: {e}")

    # 4. IndexError
    try:
        lst = [1, 2, 3]
        print(lst[10])
    except IndexError as e:
        exceptions_demo.append(f"4. IndexError: {e}")

    # 5. KeyError
    try:
        d = {"name": "Mahesh"}
        print(d["age"])
    except KeyError as e:
        exceptions_demo.append(f"5. KeyError: {e}")

    # 6. FileNotFoundError
    try:
        with open("non_existent_file.txt", "r") as f:
            pass
    except FileNotFoundError as e:
        exceptions_demo.append(f"6. FileNotFoundError: {e}")

    # 7. ModuleNotFoundError
    try:
        import non_existent_module
    except ModuleNotFoundError as e:
        exceptions_demo.append(f"7. ModuleNotFoundError: {e}")

    # 8. NameError
    try:
        print(undefined_variable)
    except NameError as e:
        exceptions_demo.append(f"8. NameError: {e}")

    # 9. AttributeError
    try:
        x = 5
        print(x.append(10))
    except AttributeError as e:
        exceptions_demo.append(f"9. AttributeError: {e}")

    # 10. ImportError (older style)
    try:
        from math import non_existent_function
    except ImportError as e:
        exceptions_demo.append(f"10. ImportError: {e}")

    # 11. OverflowError
    try:
        import math
        math.exp(1000)
    except OverflowError as e:
        exceptions_demo.append(f"11. OverflowError: {e}")

    # 12. RecursionError
    def recursive():
        return recursive()
    try:
        recursive()
    except RecursionError as e:
        exceptions_demo.append(f"12. RecursionError: {e}")

    # 13. StopIteration (manually)
    try:
        it = iter([1])
        next(it)
        next(it)          # Raises StopIteration
    except StopIteration as e:
        exceptions_demo.append(f"13. StopIteration: {e}")

    # 14. KeyboardInterrupt (Simulated - comment out if you don't want to test)
    # try:
    #     raise KeyboardInterrupt("Simulated Ctrl+C")
    # except KeyboardInterrupt as e:
    #     exceptions_demo.append(f"14. KeyboardInterrupt: {e}")

    # 15. AssertionError
    try:
        assert 1 == 2, "Assertion failed"
    except AssertionError as e:
        exceptions_demo.append(f"15. AssertionError: {e}")

    # 16. Custom Exception Example
    class CustomError(Exception):
        pass

    try:
        raise CustomError("This is my custom exception!")
    except CustomError as e:
        exceptions_demo.append(f"16. CustomError: {e}")

    # 17. General Exception (catch-all - last resort)
    try:
        raise RuntimeError("Some runtime error")
    except Exception as e:          # Broad catch
        exceptions_demo.append(f"17. General Exception: {type(e).__name__} - {e}")

    # Print all results
    print("All exceptions demonstrated successfully!\n")
    for demo in exceptions_demo:
        print(demo)

    print("\n✅ Script completed - All major exceptions covered!")


# ==================== RUN THE DEMO ====================
if __name__ == "__main__":
    demo_exceptions()