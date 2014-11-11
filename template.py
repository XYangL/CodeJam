class Solution:
	def __init__(self):
		self.re = 0

	def main(self):
		
		return self.re


fo = open("input", "r")
lines = fo.read().splitlines()
fo.close()
T = int(lines[0])

ous = ""
index = 1
for caseNum in range(T):
	N = int(lines[index])
	index +=1

	ins = lines[index:index+N]
	# print ins,'\n-----'
	index += N
	
	# for i in ins:
	# 	print i
	
	# ous +="Case #"+str(caseNum+1)+": "
	# s = Solution()
	# ous += str(s.main())
	# ous += '\n'
	
fo = open("-small.out", "w")
fo.write(ous)
fo.close()
