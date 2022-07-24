names = ["Deepak", "Ravi", "Vikas"]


# input n = 10
# queries = [[1,5,3], [4,8,8], [6,9,1]]
# print(max(names))

# queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
# queries = [[2,6,8], [3,5,7], [1,8,1], [5,9,15]]
# queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]


def arrayManipulation(n, queries):
    list = [0] * n

    for query in queries:
        for i in range(query[0] - 1, query[1]):
            list[i] += query[-1]

    return max(list)


queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
print(arrayManipulation(10, queries))

queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
print(arrayManipulation(10, queries))

queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
print(arrayManipulation(5, queries))
