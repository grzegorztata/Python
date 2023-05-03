five_divided = []
three_cubes = []

for i in range(0, 101):
    if i % 5 == 0:
        five_divided.append(i)

for i in five_divided:
    three_cubes.append(i**3)

print(five_divided)
print(three_cubes)