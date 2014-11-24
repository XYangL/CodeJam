class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def setDemo(self):
	# NLR  :  A B D C E G H F I
	# LNR  :  D B A G E H C F I
	# LRN  :  D B G H E I F C A
		n1l = TreeNode('B')
		n1l.left = TreeNode('D')

		n1rl = TreeNode('E')
		n1rl.left = TreeNode('G')
		n1rl.right = TreeNode('H')

		n1rr = TreeNode('F')
		n1rr.right = TreeNode('I')

		n1r = TreeNode('C')
		n1r.left = n1rl
		n1r.right = n1rr

		self.val = 'A' #= TreeNode('A')
		self.left = n1l
		self.right = n1r
 

	def level_order(self):
		re = []
		if self!= None:
			stack =[self]
			while len(stack)!=0:
				temp = stack[0]
				re.append(temp.val)
				stack = stack[1:]
				if temp.left:
					stack.append(temp.left)
				if temp.right:
					stack.append(temp.right)

		return re


# demo = TreeNode(0)
# demo.setDemo()
# print demo.level_order()