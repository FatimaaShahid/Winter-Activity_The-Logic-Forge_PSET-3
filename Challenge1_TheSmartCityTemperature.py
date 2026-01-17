def solve():
    import sys
    input = sys.stdin.readline

    N, K, Q = map(int, input().split())
    temp = list(map(int, input().split()))


    next_warmer = [-1] * N
    stack = []
    for i in range(N):
        while stack and temp[i] >= temp[stack[-1]] + K:
            idx = stack.pop()
            next_warmer[idx] = i
        stack.append(i)

    next_colder = [-1] * N
    stack = []
    for i in range(N):
        while stack and temp[i] <= temp[stack[-1]] - K:
            idx = stack.pop()
            next_colder[idx] = i
        stack.append(i)

    alert = [0] * N
    for i in range(N):
        w = next_warmer[i]
        c = next_colder[i]

        if w != -1 and c != -1:
            alert[i] = min(w, c)
        elif w != -1:
            alert[i] = w
        elif c != -1:
            alert[i] = c
        else:
            alert[i] = 0


    prefix = [0] * N
    prefix[0] = 1 if alert[0] != 0 else 0
    for i in range(1, N):
        prefix[i] = prefix[i - 1] + (1 if alert[i] != 0 else 0)

    
    for _ in range(Q):
        query = input().split()

        if query[0] == "NEXT":
            x = int(query[1])
            if alert[x] == 0:
                print("No Alert")
            else:
                print(alert[x])

        else:  
            L, R = map(int, query[1:])
            if L == 0:
                print(prefix[R])
            else:
                print(prefix[R] - prefix[L - 1])
