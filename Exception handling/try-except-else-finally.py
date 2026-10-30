# else block executes if there is no exception
try:
    result = 10 / 2
except ZeroDivisionError:
    result = 0
else:
    print("Result is:", result)
finally:
    print("Execution complete.")

data = {"a": 1}
try:
    val = data["a"]
except KeyError:
    val = None
else:
    print("Found value:", val)
finally:
    print("Cleanup done.")
