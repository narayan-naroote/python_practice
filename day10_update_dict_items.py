# Dictionary Example: Karnataka Famous Foods

# Initial dictionary with city-food mapping
karnataka_foods = {
    "Bengaluru": "neer dose",
    "Mysuru": "mysuru pak",
    "Davangere": "benne dose",
    "Gokak": "karadantu"
}

# Print original dictionary
print("Original Dictionary:")
print(karnataka_foods)
print()

# New dictionary to be added
new_dishes = {
    "Hubballi": "girmit"
}

# Updating dictionary using update() method
karnataka_foods.update(new_dishes)

# Print updated dictionary
print("Updated Dictionary:")
print(karnataka_foods)