boy_name = input("Enter his name: ").lower()
girl_name = input("Enter girl name: ").lower()
couple = boy_name+girl_name
t = couple.count("t")
r = couple.count("r")
u = couple.count("u")
e = couple.count("e")
true = t+r+u+e
l = couple.count("l")
o = couple.count("o")
v = couple.count("v")
e = couple.count("e")
love = l+o+v+e
true_love = str(true)+str(love)
print(f"love score: {true_love}")
