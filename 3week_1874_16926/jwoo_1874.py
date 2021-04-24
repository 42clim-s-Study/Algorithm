import sys

n = int(input())
seq = [int(sys.stdin.readline().strip()) for _ in range(n)]

def stack_seq(n, seq):
	num, point = 1, 0
	stack = []
	answer = []
	while (num <= n and point < n):
		if (num <= n and len(stack) == 0):
			stack.append(num)
			answer.append('+')
			num += 1
		while (num <= n and stack[-1] != seq[point]):
			stack.append(num)
			answer.append('+')
			num += 1
		while (point < n and len(stack) > 0 and stack[-1] == seq[point]):
			stack.pop()
			answer.append('-')
			point += 1
		if (num > n and len(stack) > 0 and stack[-1] != seq[point]):
			answer.clear()
			answer.append('NO')
			break
	return(answer)

for factor in stack_seq(n, seq):
	print(factor)