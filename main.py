# Classes
# Key-Value pair class
class keyValuePair:
    def __init__(self):
        self.store = []
    
    def SET(self, key, value):
        # Checks if key is already stored
        for i in range(len(self.store)):
            k, v = self.store[i]
            if k == key:
                self.store[i] = (key, value)
                return
        
        # Append otherwise
        self.store.append((key, value))

    def GET(self, key):
        # Returns value from store
        for k, v in self.store:
            if k == key:
                return v
        return None

# Persistent Storage, or reads/appends data to data.db and kv-pair
class persistentStorage:
    def __init__(self, filename):
        self.filename = filename
        self.kv = keyValuePair()
        self.replay_log()

    def replay_log(self, command):
        file = open(self.filename, "r")
        for line in file:
            parts = line.split(" ", 2)
            
            if parts[0] == "SET":
                self.kv.SET(parts[1], parts[2])
    
    def append_log(self, command):
        file = open("SET" + self.filename, "a")
        file.write(command + "\n")

    def SET(self, key, value):
        self.append_log(f"{key} {value}")
        self.kv.SET(key, value)
    
    def GET(self, key):
        return self.kv.GET(key)

def main():
    kv = persistentStorage("data.db")

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
            kv.SET(key, value)

        if command == "GET":
            key = parts[1]
            value = kv.GET(key)
            print(value)    

main()
