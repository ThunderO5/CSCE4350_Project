# Opens database file

# Classes
# Key-Value pair class
class keyValue:
    def __init__(self):
        self.store = []
    
    def SET(key, value):
        file = open("data.db", "a")
        file.write(f"{key} {value} \n")

    def GET(self, cmdKey):
        print("Hello!")

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
        print(parts[0])
    
    
    
