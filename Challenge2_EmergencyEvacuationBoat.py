import sys
input = sys.stdin.readline

N, Q, limit = map(int, input().split())
weights = list(map(int, input().split()))
priority = list(map(int, input().split()))

priority_people = []
normal_people = []

for i in range(N):
    if priority[i] == 1:
        priority_people.append(weights[i])
    else:
        normal_people.append(weights[i])

# Correct sorting for greedy
priority_people.sort(reverse=True)   # heaviest priority first
normal_people.sort()                 # lightest normal first

boats = 0
j = 0  # pointer for normal_people

# Pair priority people with normal people
for pw in priority_people:
    if j < len(normal_people) and pw + normal_people[j] <= limit:
        boats += 1
        j += 1
    else:
        boats += 1  # priority alone

# Pair remaining normal people
remaining = normal_people[j:]
l, r = 0, len(remaining) - 1

while l <= r:
    if l < r and remaining[l] + remaining[r] <= limit:
        l += 1
        r -= 1
    else:
        r -= 1
    boats += 1

min_boats = boats

print(f"Minimum boats = {min_boats}")


for _ in range(Q):
    cmd = input().split()

    if cmd[0] == "CANPAIR":
        x, y = int(cmd[1]), int(cmd[2])

        if x == y:
            print("No")
        elif weights[x] + weights[y] > limit:
            print("No")
        elif priority[x] == 1 and priority[y] == 1:
            print("No")
        else:
            print("Yes")

    else:  
        B = int(cmd[1])
        evacuated = min(N, 2 * B)
        print(N - evacuated)
