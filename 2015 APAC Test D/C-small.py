class Solution:
	def main(self, num, flight):
		re = []

		while len(flight)!=0 :
			for temp in flight.items():
				if not flight.has_key(temp[1]):
					break
			re = [(temp[0],temp[1])]+re
			del flight[temp[0]]
		return re

ous = ""
fo = open("C-small-attempt0.in", "r")
ins = fo.read()
ins = ins.splitlines()
fo.close()
Case_num = int(ins[0])
i = 1
for cn in range(Case_num):
	tickets_num =int(ins[i])
	i +=1
	flight = {}
	for j in range(tickets_num):
		flight[ins[i+2*j]]=ins[i+2*j+1]


	i = i+ tickets_num*2

	ous +="Case #"+str(cn+1)+":"
	s = Solution()
	for re in s.main(tickets_num,flight):
		# print re
		ous += ' '+re[0]+'-'+re[1]
	ous +='\n'
	
fo = open("C-small.out", "w")
fo.write(ous)
fo.close()
