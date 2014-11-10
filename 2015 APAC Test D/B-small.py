class Solution:
	def main(self,GBues_num,GBues_from,GBues_to,city_num,cities):
		re = [0]* city_num
		for i in range(GBues_num):
			for j in range(city_num):
				if cities[j]>=GBues_from[i] and cities[j]<=GBues_to[i]:
					re[j] +=1
		return re

ous = ""
fo = open("B-small-attempt0.in",'r')
ins = fo.read()
ins = ins.splitlines()
fo.close()
Case_num = int(ins[0])
i = 1
for cn in range(Case_num):
	GBues_num= int(ins[i])
	i +=1

	GBues_from = [0]*GBues_num
	GBues_to = [0]* GBues_num
	lines =  ins[i].replace(' ','\n').splitlines()
	i +=1
	for j in range(GBues_num*2):
		if j %2 == 0:
			GBues_from[j/2] = int(lines[j])
		else:
			GBues_to[j/2] = int(lines[j])

	city_num = int(ins[i])
	i+=1

	cities = ['0']*city_num
	for j in range(city_num):
		cities[j] = int(ins[i])
		i+=1
	i +=1
	
	# print GBues_num
	# print GBues_from
	# print GBues_to
	# print city_num
	# print cities
	
	ous +="Case #"+str(cn+1)+":"
	s = Solution()
	re = s.main(GBues_num,GBues_from,GBues_to,city_num,cities)
	for r in re:
		ous += ' ' +str(r)
	ous += '\n'
	
fo = open("B-small.out", "w")
fo.write(ous)
fo.close()
