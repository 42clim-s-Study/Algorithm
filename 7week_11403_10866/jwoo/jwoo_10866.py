import sys
from collections import deque

class Mydeque:
	def __init__(self):
		self.deque = deque()
		return

	def push_front(self, num):
		self.deque.appendleft(num)
		return

	def push_back(self, num):
		self.deque.append(num)
		return

	def pop_front(self):
		if (len(self.deque) == 0):
			return -1
		return (self.deque.popleft())

	def pop_back(self):
		if (len(self.deque) == 0):
			return -1
		return (self.deque.pop())

	def size(self):
		return (len(self.deque))

	def empty(self):
		return (int(len(self.deque) == 0))

	def front(self):
		if (len(self.deque) == 0):
			return -1
		return (self.deque[0])
	
	def back(self):
		if (len(self.deque) == 0):
			return -1
		return (self.deque[-1])


n = int(input())
commands = [sys.stdin.readline().rstrip() for _ in range(n)]

def	ft_deque(n, commands):
	deque = Mydeque()
	for i in range(n):
		if (commands[i].startswith('push_front') == 1):
			deque.push_front(commands[i].split(' ')[1])
		elif (commands[i].startswith('push_back') == 1):
			deque.push_back(commands[i].split(' ')[1])
		elif (commands[i] == 'pop_front'):
			print(deque.pop_front())
		elif (commands[i] == 'pop_back'):
			print(deque.pop_back())
		elif (commands[i] == 'size'):
			print(deque.size())
		elif (commands[i] == 'empty'):
			print(deque.empty())
		elif (commands[i] == 'front'):
			print(deque.front())
		elif (commands[i] == 'back'):
			print(deque.back())
	return

ft_deque(n, commands)