from TreeNode import TreeNode
# http://www.gocalf.com/blog/traversing-binary-tree.html
# Using iterative/loop to traverse tree in pre/in/post order
# need a STACK to store the visited but not printed nodes 
def visitTree_Iterative(root, order):
	re = []
	if order == 'NLR':
		# init a stack with root
		# use a while loop if stack!=NONE
		# in the loop, pop and print first and then push RIGHT & LEFT
		stack = [root]
		while len(stack) != 0:
			temp = stack.pop()
			re.append(temp.val)
			
			if temp.right != None:
				stack.append(temp.right)
			
			if temp.left != None:
				stack.append(temp.left)
	elif order == 'LNR':
		# init a stack, and 
		# using a while loop if root!=NONE or stack!=NONE, in the loop, 
		# update root to the most left node, and push the passed nodes
		# if no left more, pop from the stack (#!no left or left has been handled!#),
		# and print its val
		# then update root to the right
		stack = []
		while root!= None or len(stack)!=0:
			if root != None:
				stack.append(root)
				root = root.left
			else:
				root = stack.pop() # poped is no left or left has been handled
				re.append(root.val)
				root = root.right
	elif order =='LRN':
		# after handle all left children or after handle all right children
		# BOTH will make self = stack.pop()
		stack = []
		pre = None
		while root!=None or len(stack)!=0:
			if root != None:
				stack.append(root)
				root = root.left
			elif stack[-1].right!=pre:# poped is no left or left has been handled
				root = stack[-1].right
				pre = None
			else:
				pre = stack.pop()
				re.append(pre.val)


	return re

		
demo = TreeNode(0)
demo.setDemo()

order = ['NLR','LNR','LRN']
for i in order:
	print i,' : ',
	for ch in visitTree_Iterative(demo,i):
		print ch,
	print