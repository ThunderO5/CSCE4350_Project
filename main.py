import os   # Imports OS for file paths

# Classes
# Key-Value Pair Class
# Manual implementation of dictionaries using arrays
class KeyValuePair:
    def __init__(self):
        self.store = []
    
    def set(self, key, value):
        # Checks if key is already stored
        for i in range(len(self.store)):
            k, v = self.store[i]
            if k == key:
                self.store[i] = (key, value)
                return
        
        # Append otherwise
        self.store.append((key, value))

    def get(self, key):
        # Returns value from store, if exists
        for k, v in self.store:
            if k == key:
                return v
        # Otherwise, returns nothing
        return ""

# Persistent Storage
# Reads and appends key-value pairs to data.db,
# and stores key-value pairs to memory.
class PersistentStorage:
    def __init__(self, filename):
        self.filename = filename
        self.kv = KeyValuePair()

        # Creates data.db if not found
        if not os.path.exists("data.db"):
            open(filename, "a")

        self.replay_log()

    # Reconstructs the database from previous inputs
    def replay_log(self):
        with open(self.filename, "r") as file:
            for line in file:
                parts = line.split(" ", 2)
                if parts[0] == "SET":
                    self.kv.SET(parts[1], parts[2])
    
    # Appends commands to the database
    def append_log(self, command):
        with open(self.filename, "a") as file:
            file.write(command + "\n")

    # Sets keys and values to the database, then memory
    def set(self, key, value):
        self.append_log(f"{key} {value}")
        self.kv.set(key, value)
    
    def get(self, key):
        return self.kv.get(key)

def main():
    kv = PersistentStorage("data.db")

    # Loops through system input
    while True:
        line = input()
        parts = line.split(" ", 2)
        command = parts[0]

        if command == "EXIT":
            break

        if command == "SET":
            key = parts[1]
            value = parts[2]
            kv.set(key, value)

        if command == "GET":
            key = parts[1]
            value = kv.get(key)
            print(value)    

main()
