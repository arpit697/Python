name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]

z = zip(name,animal,age)

for name,animal,age in z:
    print(f"{name} is a {animal} and it`s age is {age}")