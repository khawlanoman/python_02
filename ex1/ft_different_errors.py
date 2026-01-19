def garden_operations() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        int("hi")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError...")
    arr = {"temp": 21}
    try:
        arr["missing\\_plant"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    print("Testing multiple errors together...")
    try:
        int("hi")
        10 / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


def test_error_types() -> None:
    garden_operations()


test_error_types()
