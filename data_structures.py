# 1. Dictionaries/Maps
# Big O - O(1) for lookup 

phonebook = {
    "bob": 1,
    "jill": 2,
    "pete": 3
}

squares = {x: x * x for x in range(6)}

# To get an entry in a dictionary:

print(phonebook["bob"])

# To add an entry to a dictionary:

phonebook["kathy"] = 4
print(phonebook["kathy"])

# To remove an entry to a dictionary:

phonebook.pop("test", None) # Throws KeyError if not found. NEED the None at the end
print(phonebook)

# 2. Lists/Arrays/Tuples
# Tuples are immutable, lists are mutable
# Tuples are used for multiple asimilar items, lists are used for multiple similar items
# Big O - O(n) for lookup 

user_credentials = [ # A list of tuples
    ('name', 'username', 'password'),
    ('jason', 'jsnasm', 'pword123'),
    ('mark', 'titus', 'tituspassword1'),
    ('tate', 'frazier', 'tatef455')
]

# To remove an entry by value

try:
    user_credentials.remove(('nafdme', 'username', 'password')) # Throws ValueError if not found
except ValueError:
    print("Could not find the key")
    
print(user_credentials)


# To remove an entry by index

animals.pop(2)

print(animals)