from TreeNode import TreeNode
# http://www.gocalf.com/blog/traversing-binary-tree.html
# Using Recursive to traverse tree in pre/in/post order
# - need call visitTree twice recursively
# - need a proper position to print self.val
re = []
def visitTree_Recursive(root, order):
	if root == None:
		return
	if order == "NLR": re.append(root.val)
	
	visitTree_Recursive(root.left,order)
	
	if order == "LNR": re.append(root.val)
	
	visitTree_Recursive(root.right,order)
	
	if order == "LRN": re.append(root.val)

demo = TreeNode(0)
demo.setDemo()

order = ['NLR','LNR','LRN']
for i in order:
	print i,' : ',
	re = []
	visitTree_Recursive(demo,i)
	for ch in re:
		print ch,
	print 
# NLR  :  A B D C E G H F I
# LNR  :  D B A G E H C F I
# LRN  :  D B G H E I F C A