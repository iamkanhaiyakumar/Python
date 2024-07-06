# Tuples Methods

a = (1, 2, 3, 4, 5)

# 1. count() - Returns the number of times a specified element appears in the tuple
count = a.count(3)
print(count)

# 2. index() - Returns the index of the first occurrence of a specified element in the tuple
index = a.index(4)
print(index)

# 3. len() - Returns the length of the tuple
length = len(a)
print(length)

# 4. max() - Returns the largest element in the tuple
maximum = max(a)
print(maximum)

# 5. min() - Returns the smallest element in the tuple
minimum = min(a)
print(minimum)

# 6. sorted() - Returns a new sorted list from the elements in the tuple
sorted_tuple = sorted(a)
print(sorted_tuple)

# 7. reversed() - Returns a new reversed iterator object from the elements in the tuple
reversed_tuple = tuple(reversed(a))
print(reversed_tuple)

# 8. any() - Returns True if at least one element in the tuple is true, otherwise False
any_true = any(a)
print(any_true)

# 9. all() - Returns True if all elements in the tuple are true, otherwise False
all_true = all(a)
print(all_true)

# 10. tuple() - Converts an iterable object into a tuple
list1 = [1, 2, 3, 4, 5]
tuple1 = tuple(list1)
print(tuple1)