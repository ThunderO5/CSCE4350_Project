# Opens database file
file = open("data.db", "a")

# Classes
# Key-Value pair class
class keyValue:
    def __int__(self, key, value):
        self.key = key
        self.value = value

# Loops through system input
while True:
    cmd = input("Enter commands (SET, GET, EXIT): ")
    if cmd == "EXIT":
        break
    print(cmd)
