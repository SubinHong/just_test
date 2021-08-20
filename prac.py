from collections import deque


def DFS(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and adj[v][i] == 1:
            DFS(i)


def BFS(v):
    queue = deque()
    visit[v] = 1
    queue.append(v)
