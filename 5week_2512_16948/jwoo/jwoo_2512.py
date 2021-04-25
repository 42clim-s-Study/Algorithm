import sys

n = int(input())
region = list(map(int, sys.stdin.readline().split()))
m = int(input())

def budget_distribution(region, n, m):
	if (sum(region) <= m):
		return max(region)
	start = 1
	end = max(region)
	while start <= end:
		mid = (start + end) // 2
		budget = 0
		for request in region:
			if request <= mid:
				budget += request
			else:
				budget += mid
		if budget < m:
			start = mid + 1
		elif budget > m:
			end = mid - 1
		else:
			return mid
	return end

print(budget_distribution(region, n, m))
