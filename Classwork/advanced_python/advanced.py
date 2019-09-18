# ls1 = [i for i in range(100000000)]

# print(ls1[0])

ls2 = (i for i in range(100000000))

# print(ls2[0])


def printing_generator():
    ls3 = (i for i in range(1000000))

    for elem in ls3:
        print(elem)

    print("second time should print NOTHING!")
    for elem in ls3:
        print(elem)

# printing_generator()


def generator_ex(ls):
    s = 0
    for i in ls:
        s += i
        yield s

G = generator_ex([1, 2, 3, 4])

for item in G:
    print(item)

