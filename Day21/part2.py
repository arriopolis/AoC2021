import sys
import itertools as it

poss = [int(line.strip()[28:]) for line in sys.stdin]
scores = [0,0]
ctr = 0
turn = 1

rolls = {}
for d1,d2,d3 in it.product(range(1,4), repeat = 3):
    d = d1 + d2 + d3
    if d not in rolls: rolls[d] = 0
    rolls[d] += 1

dp = {((0,0),tuple(poss),0) : 1}
to_visit = {(0,0) : set([((0,0),tuple(poss),0)])}
win1,win2 = 0,0
for t1 in range(21):
    for t2 in range(21):
        if (t1,t2) not in to_visit: continue
        for state in to_visit[(t1,t2)]:
            (s1,s2),(p1,p2),turn = state
            for d,k in rolls.items():
                if turn == 0 and s1+((p1+d-1)%10)+1 >= 21:
                    win1 += k * dp[state]
                    continue
                elif turn == 1 and s2+((p2+d-1)%10)+1 >= 21:
                    win2 += k * dp[state]
                    continue

                if turn == 0:
                    new_state = (s1+((p1+d-1)%10)+1,s2),((p1+d-1)%10+1,p2),1
                else:
                    new_state = (s1,s2+((p2+d-1)%10)+1),(p1,(p2+d-1)%10+1),0

                if new_state[0] not in to_visit: to_visit[new_state[0]] = set()
                to_visit[new_state[0]].add(new_state)

                if new_state not in dp: dp[new_state] = 0
                dp[new_state] += k * dp[state]
print(max(win1, win2))
