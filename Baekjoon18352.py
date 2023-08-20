# Baekjoon 18352 특정 거리의 도시 찾기
# DFS, BFS 둘다 써야하는 것 같은데..!
# X에서 출발해서 다른 노드로 가는 최단거리가 K인 노드를 출력
# https://www.acmicpc.net/problem/18352

# 최단거리 문제는 BFS를 쓰자!
class Queue:
    front = -1
    rear = -1
    def __init__(self, size):
        self.q = [0] * size

    def enqueue(self, item):
        self.rear += 1
        self.q[self.rear] = item

    def dequeue(self):
        self.front += 1
        return self.q[self.front]

    def isEmpty(self):
        return self.front == self.rear

# 주석처리한 부분은 deque를 사용하는 부분
import sys
#from collections import deque
input = sys.stdin.readline
N, M, K, X = map(int, input().split()) # 도시 개수, 도로 개수, 최단 거리, 시작 도시 번호
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    edge = list(map(int, input().split()))
    adj_list[edge[0]].append(edge[1])

def BFS(X, K):
    #queue = deque([])
    #queue.append(X)
    queue = Queue(M+3)
    queue.enqueue(X)
    visited[X] = 0
    #while queue:
    while not queue.isEmpty():
        #n = queue.popleft()
        n = queue.dequeue()
        if visited[n] > K+1:
            return

        for w in adj_list[n]:
            if visited[w] == -1:
                #queue.append(w)
                queue.enqueue(w)
                visited[w] = visited[n] + 1
                if visited[w] == K:
                    ans.append(w)

visited = [-1] * (N+1)
ans = []
BFS(X, K)

ans.sort()
if ans:
    for i in ans:
        print(i)
else:
    print(-1)