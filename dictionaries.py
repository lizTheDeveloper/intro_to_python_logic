pets = {
    "cat": 1,
    "dog": 1,
    "fish": 37
}

for pet, number in pets.items():
    print(pet,number)


print("birds", pets.get("birds", 0))



user = {
    'username': "LizTheDeveloper",
    "email": "liz@themultiverse.school",
    "title": "I'm CEO",
    "customer_details" : {
        "client": "Multiverse",
        "last_login": "May 23"
    }
}

user["title"] = "CTO"
print(user["customer_details"]["client"])

