from functools import reduce
from collections import Counter
intersection = reduce(lambda x, y: x & y, [{3, 4}, {3, 5}, {5 ,7}])

print(intersection)

words = ["Deer", "Bear", "River", "Car", "Car", "River", "Deer", "Car", "Bear"]

# implement histogram using map and reduce

mapping = list(map(lambda x: {x: 1}, words))
print((mapping))
# reduced = reduce(lambda x, y: x[]+y if x != y else x, mapping)

# print(reduced)