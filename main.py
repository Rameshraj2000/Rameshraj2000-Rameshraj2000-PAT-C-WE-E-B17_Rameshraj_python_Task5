people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 16},
    {"name": "Eve", "age": 22}
]

# Step 1: Filter people who are 18 or older using lambda
# filter() keeps items where the lambda returns True
adults = list(filter(lambda person: person["age"] >= 18, people))

# Step 2: Map to get only the names of adults
# map() applies lambda to each item, extracting the name
adult_names = list(map(lambda person: person["name"], adults))

# Or you can do it in one line (but separate steps are clearer for beginners):
# adult_names = list(map(lambda p: p["name"], filter(lambda p: p["age"] >= 18, people)))

print("Adults (18+):", adults)
print("Adult names:", adult_names)