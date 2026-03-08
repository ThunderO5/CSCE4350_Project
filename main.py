# Opens database file

# Classes
# Key-Value pair class
class keyValue:
    def __init__(self):
        self.store = []
    
    def SET(key, value):
        file = open("data.db", "a")
        file.write(f"{key} {value} \n")

    def GET(key):
        file = open("data.db", "r")
        for line in file:
            parts = line.split(" ")
            if parts[0] == key:
                return parts[1]

kv = keyValue

# Loops through system input
while True:
    line = input("Enter commands (SET, GET, EXIT): ")
    parts = line.split(" ", 2)
    command = parts[0]

    if command == "EXIT":
        break
    if command == "SET":
        key = parts[1]
        value = parts[2]
        kv.SET(key, value)
    if command == "GET":
        key = parts[1]
        value = kv.GET(key)
        print(value)    
