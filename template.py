class Solution:
	def main(self):

		return re


ous = ""
fo = open("input", "r")
ins = fo.read()
ins = ins.splitlines()
fo.close()
Case_num = int(ins[0])
i = 1
for cn in range(Case_num):

	
	ous +="Case #"+str(cn+1)+": "
	s = Solution()
	ous += str(s.main())
	ous += '\n'
	
fo = open("output", "w")
fo.write(ous)
fo.close()
