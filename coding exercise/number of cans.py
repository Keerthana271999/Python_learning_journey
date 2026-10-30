print("Number of cans required")
print("Assume 1 can covers 7 m^2")


def coverage():
    height = float(input("Enter height of the wall (m): "))
    width = float(input("Enter width of the wall (m): "))
    can = 7
    area = height*width
    required = area/can
    print(f"Number of cans required to paint the wall: {required}")


coverage()
