import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

case, i, j = 0, 0, 1
while i < n and j <= n and i < j:
	temp = sum(a[i:j])
	if temp < m:
		j += 1
	elif temp > m:
		i += 1
	else:
		case += 1
		j += 1
	if i == j and i != n:
		j += 1

print(case)