f=open('Day 5\File.txt',"w")
data=f.read()
f.write("Are you Happy")
print(data)
f.close()

f=open("Day 5\File.txt","a")
f.write("This is new text")
f.close()

f=open("file2.txt","x")
f.write("Open new files which name is 2")
f.close()

with open("Day 5\File.txt",'r') as f:
    data=f.read()
    print(data)

import os
os.remove("file2.txt")

data=True
with open('Day 5\File.txt','r') as f:
    while data:
        data=f.read()
        print(data)

try:
    x=int(input("Enter Number: "))
    ans=10/x
except ZeroDivisionError:
    print("This is not Allowed")
else:
    print(f"Answer: {ans}")

with open('Code.txt','w') as file:
    for i in range(5):
        name=input("Enter Name: ")
        file.write(name + '\n')
print("\nNames in File\n")

with open('Code.txt','r') as file:
    print(file.read())

with open("log.txt",'a') as file:
    file.write("This is log 1")
    

with open("log.txt",'r') as file:
    data=file.read()
    print(data)


