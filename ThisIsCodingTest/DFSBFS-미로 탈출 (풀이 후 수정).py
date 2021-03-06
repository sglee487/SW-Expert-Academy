from collections import deque
import sys

sys.stdin = open("DFSBFS-미로 탈출.txt", "r")

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

# 위 오 아래 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

Q = deque()
Q.append((0,0,1))
result = -1
while Q:
    r, c, move = Q.popleft()
    if (r,c) == (N-1,M-1):
        break
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if (0<=nr<N and 0<=nc<M) and board[nr][nc] == 1 and not (nr == 0 and nc == 0):
            Q.append((nr,nc,move+1))
            board[nr][nc] = move+1
print(*board,sep='\n')
print(board[N-1][M-1])