# This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula: If there are less than a hundred points on the card, the bonus is 10 %. In any other case the bonus is 15 %

'''
E.g. You are an emplaye you get salaray. At the end of the year you get hike of x% = (x% of existing salary) + salary = total salary. same applies here
(x% of existing salary) = salaray after hike
(x% of existing salary) + salary = total salary including hike
'''

points = int(input("How many points are there on the card? "))
if points < 100:
    bonus_percent = 10
else:
    bonus_percent = 15
bonus = (bonus_percent/100)*points
total_points = points+bonus
print("Total points:", total_points)
