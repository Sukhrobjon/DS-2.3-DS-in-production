def addOne(myFunc):
    def addOneInside(x):
        print("adding One")
        return myFunc(x) + 1
    return addOneInside


@addOne
def subThree(x):
    return x - 3

# result = addOne(subThree)
# print(subThree(5))
# print(result(5))
# uncomment this if decorator is used
# print(subThree(5))


# =============================================================== #

def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# this slows down the run time, because it is not using memoize function
# it is just using the recursive function
# result = memoize(fib)
# print(result(40))

# when we name it same as function name it uses memoize
fib = memoize(fib)
# print(fib(40))


# =============================================================== #
def call(*argv, **kwargs):
    def call_fn(fn):
        return fn(*argv, **kwargs)
    return call_fn


@call(5)
def table(n):
    value = []
    for i in range(n):
        value.append(i*i)
    return value


# table = call(5)(table)
# print(table)
# print(len(table), table[3])


def set_intersection(*args):
    """Finds intersection of n number of sets"""
    result = set(args[0])
    for i in range(1, len(args)):
        result = result & args[i]
    return result


print(set_intersection({3, 4}, {3, 5}, {5, 7}))
