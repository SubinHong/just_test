from collections import deque
import sys

# 컴퓨터 수 입력받기
n = int(sys.stdin.readline())

# 연결된 쌍수 입력받기
pair = int(sys.stdin.readline())

computer = [[]*n for _ in range(n+1)]   # 컴퓨터를 담을 배열 생성

for i in range(pair):
    a, b = map(int, sys.stdin.readline().split())
    computer[a].append(b)   # 연결된 컴퓨터 번호 쌍을 배열에 추가
    computer[b].append(a)
    # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

# 감염대수 누적변수
cnt = 0

# 바이러스 감염여부 확인할 리스트 만들기(컴퓨터 번호 쉽게 알기 위해 n+1)
infected = [0]*(n+1)


def dfs(start):  # 감염된 컴퓨터 1을 함수 인자로 받음
    global cnt
    # 컴퓨터 1은 감염된거 알고 있으니까 미리 컴퓨터1번 자리에 1 추가
    infected[start] = 1

    # 1번~7번 컴퓨터와 각각 쌍인 computer 목록을 순회하며 감염됐는지 여부 확인
    # 시작은 1번 컴퓨터와 연결된 1번 인덱스 요소 [2, 5]를 하나씩 꺼냄. 그 다음 [1, 3, 5] 컴퓨터 하나씩 꺼내고 반복
    for i in computer[start]:
        # 처음에 i에는 2가 들어감
        if infected[i] == 0:
            # 재귀하며 i와 start가 1씩 증가함
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)

"""실패"""
# def bfs(computer):
#     queue = deque()
#     queue.append(1)  # 1번 컴퓨터를 큐에 추가
#     count = 0
#     # 큐가 진행되는 동안
#     while queue:
#         v = queue.popleft()  # 큐에서 pop 된 원소가 곧 감염된 컴퓨터와 연결접점이 있는 컴퓨터를 찾는 매개체
#         # 현재 주어진 컴퓨터에 연결된 컴퓨터 찾기
#         for com in computer[v]:  # computer[1]부터 끝까지 원소를 하나씩 꺼내서
#             if virus[com] == 0:  # 첫 컴퓨터(원소)가 2일 때, virus 배열 인덱스 2가 0인지 확인
#                 virus[com] = 1  # 감염된 것으로 판단하여 해당 컴퓨터가 감염된 것으로 판단
#                 queue.append(com)
#                 count += 1  # 큐에 감염 컴퓨터를 인큐했다면 카운트 해줌
#     return count
