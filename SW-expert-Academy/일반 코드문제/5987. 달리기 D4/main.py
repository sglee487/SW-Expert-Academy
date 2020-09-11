import sys

sys.stdin = open("s_input.txt", "r")

def dfs(now):
    if now == end: return 1
    if cases[now] : return cases[now]
    for i in range(N):
        if now & (1 << i) == 0 and (now & left[i]) == left[i]:
            cases[now] += dfs(now | (1 << i))
    return cases[now]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())

    left = [0] * N
    cases = [0] * (1 << N)
    for _ in range(M):
        a, b = map(int, input().split())
        left[b-1] |= 1 << (a-1)

    end = (1<<N) - 1

    result = dfs(0)

    print("#{0}".format(test_case), result)
    # ///////////////////////////////////////////////////////////////////////////////////
