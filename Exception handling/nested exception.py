try:
    print("Outer Try Start")

    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Inner Except: Division by zero")
    else:
        print("Inner Else: Result is", result)
    finally:
        print("Inner Finally: Math block done")

    risky_operation = int("not_a_number")

except ValueError:
    print("Outer Except: Invalid conversion caught by outer layer")
else:
    print("Outer Else: Everything succeeded without outer errors")
finally:
    print("Outer Finally: All processes terminated")


try:
    x = int("abc")
except ValueError:
    print("Outer Except Start")
    try:
        y = 10 / 0
    except ZeroDivisionError:
        print("Nested Except: Handled inner division error")
    finally:
        print("Nested Finally: Inner cleanup done")
finally:
    print("Outer Finally: Main cleanup done")


try:
    outer_file = open("data.txt", "r")
except FileNotFoundError:
    print("Outer Except: File missing")
else:
    try:
        content = outer_file.read()
        value = int(content)
    except ValueError:
        print("Inner Except: Cannot convert to int")
    else:
        print("Inner Else: Value is", value)
    finally:
        outer_file.close()
        print("Inner Finally: File closed")
finally:
    print("Outer Finally: Execution complete")


try:
    print("Main Try Block")
    result = 10 / 2
except ZeroDivisionError:
    print("Main Except Block")
finally:
    print("Main Finally Block: Starting nested block...")
    try:
        file = open("temp.txt", "r")
    except FileNotFoundError:
        print("Nested Except Block: File not found during cleanup")
    finally:
        print("Nested Finally Block: Cleanup complete")
