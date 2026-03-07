import sys  # Imports SYS module for command line input and output
import os   # Imports OS module for database 

# Opens database file
file = os.open("data.db", os.O_RDWR | os.O_CREAT)

# Loops through system input
for i in sys.stdin:
    if i[0:3] == "SET":
        print(i)
    if i[0:3] == "GET":
        print(i)
    if i[0:4] == "EXIT":
        break
