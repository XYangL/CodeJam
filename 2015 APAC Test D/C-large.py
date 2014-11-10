class Solution:
	def main(self, num, flight):
		re = []

		flight_re = {}
		for i in flight.keys():
			flight_re[flight[i]]=i

		end = ''
		for temp in flight.items():
			if not flight.has_key(temp[1]):
				end = temp[1]
				re = [(temp[0],temp[1])]+re
				break
		
		mid =temp[0] 
		while flight_re.has_key(mid):
			re = [(flight_re[mid],mid)]+re
			mid = flight_re[mid]

		return re

ous = ""
fo = open("C-large.in", "r")
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
	
fo = open("C-large.out", "w")
fo.write(ous)
fo.close()
