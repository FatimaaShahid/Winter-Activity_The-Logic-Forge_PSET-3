
N, Q, list= map(int, input().split())
subscr={}
for u in range(N):
    subscr[u]=set()

mgs=[]
msg_id=1
for i in range(Q):
    act= input().split()
    if act[0]=="S":
        u= int(act[1])
        v=int(act[2])
        subscr[u].add(v)
    elif act[0] == "U":
        u = int(act[1])
        v = int(act[2])
        if v in subscr[u]:
            subscr[u].remove(v)
    elif act[0] == "B":
        u = int(act[1])
        m = int(act[2])
        critical = m % 3 == 0
        mgs.append((msg_id, u, critical))
        msg_id += 1
    elif act[0] == "F":
        u = int(act[1])
        feed = []
        for mid, sender, critical in mgs:
            if sender in subscr[u]:
                feed.append(mid)
        top_feed = feed[:10][::-1]

        if top_feed:
            print("Answer: ", end="")
            print(" ".join(map(str, top_feed)))
        else:
            print("Answer: ", end="")
            print("EMPTY")

