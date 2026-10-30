from user_defined_class import InvalidPin
actual = 3829
try:
    pin = int(input("Enter ATM pin: "))
    if pin == actual:
        print("Login successful")
    # so here it just raises exception as defined in class but to execute actually you are using except block

    # i.e. raise just raises exception does not execute actually the way inbuilt exception execeutes with msg
    else:
        raise InvalidPin("You entered invalid pin")
except InvalidPin as msg:
    print(f"{msg.__class__.__name__}: You entered invalid pin ")
finally:
    print("Thank you")
