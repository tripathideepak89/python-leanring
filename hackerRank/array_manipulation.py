def array_manipulation(n, queries):
    result = [0] * (n + 1)
    for query in queries:
        if query[0] > 0:
            result[query[0] - 1] = result[query[0] - 1] + query[-1]
        if query[1] < n:
            result[query[1]] = result[query[1]] - query[-1]

    cumulative = 0
    for i in range(n):
        if result[i] > 0:
            result[i] = result[i] + cumulative
            cumulative = result[i]

    return max(result)


# queries = [
#     [1, 5, 3],
#     [4, 8, 7],
#     [6, 9, 1]
# ]

queries = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]

print(array_manipulation(3, queries))
