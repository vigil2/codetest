stack = []

stack.append(0)
stack.append(1)
stack.pop()
stack.append(1)
stack.append(2)
stack.append(3)

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

print(stack[3:0:-1])
print(stack[0:4])

# Queue
# Queue 구현을 위해 Deque 라이브러리를 사용
from collections import deque # 리스트 자료형을 쓸 경우 시간복잡도가 높아서 아래를 불러옴

queue = deque()

queue.append(0)
queue.append(0)
queue.append(1)
queue.popleft() 
queue.append(2)
queue.append(3)

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 순서대로 출력

# 재귀함수 (ex n!, 최대공약수(greatest common deviser)(유클리드 호제법)) DFS구현할때 씀

def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서 호출", i+1, "번째 재귀함수를 호출")
    recursive_function(i+1)
    print(i, "번째 재귀함수를 종료합니다")

recursive_function(1)
