# name='Shayan'
# print(name[3:10])


name='Shayan'
# name2="Noman"
# print("My name is {1} and his is {0}".format(name,name2))

# print(f"Name is {name}")

list=[1,2,3,4,5]
# print(list)
# print(list[:])

list.append(6)
# print(list)
list.insert(0,0)
print(list)
list.reverse()
print(list)

marks = [42, 45, 47, 41, 39]
target = 47

for i in range(len(marks)):
    if marks[i] == target:
        print(f"{target} is stored at index {i}")
        break

