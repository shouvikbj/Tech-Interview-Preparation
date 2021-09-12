def findFib(N, diary={1: 0, 2: 1}):
    if N in diary:
        return diary[N]
    else:
        diary[N] = findFib(N - 1, diary) + findFib(N - 2, diary)
        return diary[N]


print(findFib(9))
