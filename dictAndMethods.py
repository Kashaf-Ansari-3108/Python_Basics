# a = {}
# b = set()
# print(a, type(a))
# print(b, type(b))

dict1 = {"good":"Something pleasant",
         "fetch":"to bring",
         "1":"The number 1"}

ages = {"Kashaf":23, "Effat":18}
ages["Sabahat"] = 15
print(ages)
print(ages["Kashaf"])
print(dict1['good'])

print(ages.get('Kashaf Ansari'))
print(ages.get('Kashaf'))
print(ages.keys())
print(ages.values())
print(ages.items())

