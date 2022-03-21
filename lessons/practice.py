"""Just for practicing stuff."""

weights: dict[str, int] = {'Todd': 199, "Brooks": 171, "Cole": 176}


weights["Todd"] += 5

weights["Bronco"] = 175

weights["Todd"] = weights["Brooks"] + 5
print(weights)

name: dict[str, str] = {'Ch': "x", "Ch": "x"}
print(name)

if 176 == weights['Todd']:
    print("yes")

print(weights['Todd'])

names: list[str] = ['Todd', "Brooks", "Cole"]
names2: list[str] = ['Todd', "Trevor", "Cole"]

for names1 in names:
    if names1 in names2:
        print(names1)