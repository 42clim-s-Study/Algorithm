import sys

def preorder(n, tree, node):
	if tree[node][0] != '.':
		if tree[node][1] != '.':
			left = ord(tree[node][1]) - 64
		else:
			left = 0
		if tree[node][2] != '.':
			right = ord(tree[node][2]) - 64
		else:
			right = 0
		print(tree[node][0], end='')
		preorder(n, tree, left)
		preorder(n, tree, right)
	else:
		return

def inorder(n, tree, node):
	if tree[node][0] != '.':
		if tree[node][1] != '.':
			left = ord(tree[node][1]) - 64
		else:
			left = 0
		if tree[node][2] != '.':
			right = ord(tree[node][2]) - 64
		else:
			right = 0
		inorder(n, tree, left)
		print(tree[node][0], end='')
		inorder(n, tree, right)
	else:
		return

def postorder(n, tree, node):
	if tree[node][0] != '.':
		if tree[node][1] != '.':
			left = ord(tree[node][1]) - 64
		else:
			left = 0
		if tree[node][2] != '.':
			right = ord(tree[node][2]) - 64
		else:
			right = 0
		postorder(n, tree, left)
		postorder(n, tree, right)
		print(tree[node][0], end='')
	else:
		return

n = int(input())
tree = [0 for _ in range(n + 1)]
tree[0] = ['.']
for i in range(1, n + 1):
	tree[i] = list(sys.stdin.readline().split())
tree.sort()

preorder(n, tree, 1)
print()
inorder(n, tree, 1)
print()
postorder(n, tree, 1)