
# 1.
words = ["salom", "dunyo", "python"]

result = list(map(lambda x: x.upper(), words))

print(result)
# 2.
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

# 3.

words = ["salom", "dunyo", "python"]

result = list(map(lambda x: x[0], words))

print(result)

# 4.

animals = ['it', 'mushuk', 'fil']

result = sorted(animals, key=lambda x: len(x))

print(result)

# 5.  
max_num = lambda a, b: a if a > b else b

print(max_num(10, 7))

# 6.

reverse = lambda x: x[::-1]

print(reverse("python"))

# 7.

people = [("Alijon", 25), ("Valijon", 20), ("John", 30)]

result = sorted(people, key=lambda x: x[1])

print(result)

# 8.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
    