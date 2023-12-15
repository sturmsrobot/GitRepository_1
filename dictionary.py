dictionary = {
    "Schlüssel" : "Wert",
    "Hotel": "Trivagu"
}

def addItem(key, value):
    dictionary[key] = value

addItem("Horst", "Kurt")
print(dictionary["Horst"])