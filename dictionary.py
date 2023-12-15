dictionary = {
    "Schlüssel" : "Wert",
    "Hotel": "Trivagu"
}

def addItem(key, value):
    dictionary[key] = value

addItem("Horst", "Kurt")
print(dictionary["Horst"])

def printValue(key):
    if key in dictionary:
        print(dictionary[key])
    else:
        print("Key not found")

def valueIsEqual(key, value):
    return dictionary.get(key) == value

def deleteItem(key):
    if key in dictionary:
        del dictionary[key]
        print(f"Item with key ‘[key]‘ deleted.")
    else:
        print ("Key not found")
        
def printKeys():
    print("Keys in the dictionary:")
    for key in dictionary.keys():
        print(key)
        
def printValues():
    print("Values in the dictionary:")
    for value in dictionary.values():
        print(value)
        
# Commit nach jeder Teilaufgabe:
# a) "printValue":
printValue("Hotel")

# b) "valueIsEqual":
result = valueIsEqual("Schlüssel", "Wert")
print(f"Result of valueIsEqual: {result}")

# c) "deleteItem":
deleteItem("Schlüssel")

# d) "printKeys":
printKeys()

# e) "printValues":
printValues()

# Rest des Codes ausführen
addItem("Horst", "Kurt")
print(dictionary["Horst"])