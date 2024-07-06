# name = ["Apple", "Banana", "Cherry", 5, False, 3.1, "Rohan"]
# print (name)
# name.append('0505')
# print (name)


l1 = [1, 8, 7, 2, 21, 15]
# l1.sort()
# l1.reverse()
# l1.append(45)
# l1.insert(0,0)
# l1.pop(2)
# l1.remove(21)

# print(l1.pop(1))

value =l1.pop(3)
print (value)
print (l1)

# Clear the list
l1.clear()
print(l1)

# Extend the list with another list
l2 = [4, 9, 12]
l1.extend(l2)
print(l1)

# Count the occurrences of an element in the list
count = l1.count(9)
print(count)

# Get the index of the first occurrence of an element in the list
index = l1.index(12)
print(index)

# Check if an element is present in the list
is_present = 21 in l1
print(is_present)

# Get the length of the list
length = len(l1)
print(length)