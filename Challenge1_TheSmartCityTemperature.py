
N, K, Q = map(int, input().split())
temps = list(map(int, input().split()))

alert = [0] * N

for i in range(N):
    for j in range(i + 1, N):
        if temps[j] >= temps[i] + K or temps[j] <= temps[i] - K:
            alert[i] = j
            break
for _ in range(Q):
    parts = input().split()

    if parts[0] == "NEXT":
        X = int(parts[1])
        if alert[X] == 0:
            print("No Alert")
        else:
            print(alert[X])

    elif parts[0] == "COUNT":
        L = int(parts[1])
        R = int(parts[2])

        count = 0
        for i in range(L, R + 1):
            if alert[i] != 0:
                count += 1
        print(count)
