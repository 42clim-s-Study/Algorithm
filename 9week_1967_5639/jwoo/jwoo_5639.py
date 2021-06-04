import sys
sys.setrecursionlimit(10**9)

tree = []
while True:
	try:
		tree.append(int(sys.stdin.readline().strip()))
	except:
		break

def	post_order(tree):
	if len(tree) == 0:
		return
	root = tree[0]
	mid = len(tree)
	for index in range(1, len(tree)):
		if tree[index] > root:
			mid = index
			break
	post_order(tree[1:mid])
	post_order(tree[mid:])
	print(root)

post_order(tree)