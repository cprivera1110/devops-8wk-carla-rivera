# Collection: List, Tuple, Set, Dictionary

# List: a collection of items that can be changed aka is mutable, and is ordered.
fruits = ["apples","bananas","pears","grapes","oranges","pineapple","tomatoes"]
print(fruits[0]) # apples
print(fruits[1]) # bananas

fruits.append("grapefruit")
print(fruits)

fruits.remove("tomatoes")
print(fruits)

for fruit in fruits:
    if fruit == "oranges":
        print("No oranges please!")
        continue
    print(fruit)

fruits.insert(2, "kumquats")
print(fruits)

fruits.pop()
print(fruits)
print()

# Tuple: a set that cannot be changed, is immutable, and is ordered.
regions = (("us","east1"),("us","west2"),("us","east1"),("eu","west1"),("eu","east2"))
print(regions)

for region in regions:
    print(region)
print(len(regions))
print()

# Set: a collection of unique items that can be changed, is mutable, and is unordered.
# Note that for unique items, sets do not allow duplicate items
users = {"Carla", "Haiman", "Lawrence", "Josie", "Calvin", "Patrick", "Carla"}
print(users)
print(len(users))

users.add("Saket")
users.add("Calvin")
print(users)
print(len(users))

users.discard("Carla") # Duplicate value will be removed
print(users)
print(len(users))
print()

# Dictionary: a collection of key-value pairs that can be changed, mutable, and is unordered.
employee = {
    "name": "Haiman Sher",
    "age": 21,
    "salary": 100000,
    "is_trainee": True
}

print(employee["name"]) # print Haiman Sher
print(employee["is_trainee"])