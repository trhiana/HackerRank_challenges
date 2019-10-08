# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

n = int(sys.stdin.readline().strip())

phonebook = dict()

for val in range(n):
    entry = sys.stdin.readline().strip().split(" ")
    phonebook[entry[0]] = entry[1]

name = sys.stdin.readline().strip()
while name:
    number = phonebook.get(name)
    if number:
        print(name + "=" + number)
    else:
        print("Not found")
    
    name = sys.stdin.readline().strip()
