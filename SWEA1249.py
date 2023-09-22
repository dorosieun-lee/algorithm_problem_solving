# SWEA 1249 보급로

class Queue:
    maximum = 100*100*100
    front = rear = -1

    def __init__(self):
        self.queue = [0] * self.maximum

    def enqueue(self, item):
        if self.isFull():
            diff = self.rear - self.front # queue 안에 있는 내용의 크기
            self.queue[0:diff] = self.queue[self.front+1:][:]
            self.front = -1
            self.rear = diff - 1
        self.rear += 1
        self.queue[self.rear] = item

    def dequeue(self):
        self.front += 1
        return self.queue[self.front]

    def isFull(self):
        return self.rear == self.maximum - 1

    def isEmpty(self):
        return self.front == self.rear

# q = Queue()
# lst = list(range(1, 20))
# for i in lst:
#     q.enqueue(i)
#     print(q.front)
#     print(q.rear)
#     print(q.queue)
#     print('큐 출력: ', q.dequeue())


def BFS(start):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    accumulated[start[0]][start[1]] = 0
    q = Queue()
    q.enqueue(start)

    while not q.isEmpty():
        i, j = q.dequeue()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if (0 <= ni < N) and (0 <= nj < N):
                new_dist = accumulated[i][j] + MAP[i][j]
                if new_dist < accumulated[ni][nj]:
                    accumulated[ni][nj] = new_dist
                    q.enqueue((ni, nj))


T = int(input())
for test in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, list(input()))) for _ in range(N)]

    accumulated = [[float("inf")] * N for _ in range(N)]
    BFS((0,0))

    result = accumulated[-1][-1]
    print(f'#{test} {result}')