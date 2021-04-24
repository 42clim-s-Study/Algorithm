import sys
from collections import deque

string = deque(sys.stdin.readline().strip())
que = deque()
m = int(input())

for _ in range(m):
	cmd = list(sys.stdin.readline().split())
	if cmd[0] == 'L':
		if string:
			que.appendleft(string.pop())
	elif cmd[0] == 'D':
		if que:
			string.append(que.popleft())
	elif cmd[0] == 'B':
		if string:
			string.pop()
	elif cmd[0] == 'P':
		string.append(cmd[1])

print(''.join(string) + ''.join(que))