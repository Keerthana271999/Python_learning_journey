#KEYS - IMMUTABLE DATA TYPE AND UNIQUE ELSE OVERRIDES
#VALUES - MUTABLE DATA TYPE, CAN HAVE DUPLICATES
navin={
    "name":"navin",
    42:"age",
    (11111,22222):"Ph no",
    "name":"navin reddy",
    "full name":"navin reddy"
}

#FETCH USING KEYS
#IF KEY IS NOT THERE GIVES KEY ERROR
#GET METHOD RETURNS NONE BUT CAN HAVE CUSTOM MSG
print(navin["name"],navin.get("age","NA"))

del navin[(11111,22222)]
print(navin)

navin.pop("full name")
print(navin)

#NESTED 
jenny={
    "name2":"jenny",
    45:"age2",
    (1111,2222):"Ph no2",
}
navin.update(jenny)
print(navin)

navin={
    "name":"navin",
    "ph no":{"work":[1111,2222],"pers":(3333,4444)}
}
print(navin["ph no"]["pers"][1])

#EXERCISE
data = {
    'harsh': ['Java', 'Python', 'AI'],
    'navin': {'frontend': 'React', 'backend': 'Spring'},
    'kiran': ('JS', 'Flask')
}
print(data['navin']['backend'])