# Creating a dictionary
students = {
    1: 'sahil',
    2: 'teja ',
    3: 'manvitha',
    4: 'krishna',
    5: 'praveen'
}
print("Original Dictionary:", students)

# Adding a new element to the dictionary
students[6] = 'sarath'
print("\nDictionary after adding a new item:", students)

# Updating an existing value in the dictionary
students.update({3: 'Manogna'})
print("\nDictionary after updating a value:", students)

# Accessing a specific value in the dictionary
print("\nAccessing a value from the Dictionary:", students.get(1))

# Deleting an element from the dictionary
students.pop(6, None)
print("\nDictionary after deleting an item:", students)

# Creating a nested dictionary
nested_dict = {
    1: 'Teja',
    2: 'Sahil',
    3: {
        'Age': 20,
        'Branch': 'CSD',
        'Year': 'Fourth Year'
    }
}
print("\nNested Dictionary:", nested_dict)

# Accessing an element from the nested dictionary
print("\nAccessing an element from the Nested Dictionary:", nested_dict[2])
