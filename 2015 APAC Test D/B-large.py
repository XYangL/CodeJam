class Solution:
	def main(self,GBues_num,GBues_from,GBues_to,city_num,cities): 
		re = [0]* city_num
		city_i = 0
		city = cities[city_i]
		left = []
		mid = []
		right =[]

		for bus_i in range(GBues_num):
			if GBues_to[bus_i]<city:
				left.append((GBues_from[bus_i],GBues_to[bus_i]))
			elif GBues_from[bus_i]>city:
				right.append((GBues_from[bus_i],GBues_to[bus_i]))
			else:
				mid.append((GBues_from[bus_i],GBues_to[bus_i]))

			re[city_i] = len(mid)


		if city_num>1:
			city_i +=1
			while city_i < city_num:
				city = cities[city_i]
				new_left = []
				new_mid = []
				new_right = []
				if city < cities[city_i-1]:
					for bus_i in range(len(left)):
						if left[bus_i][1]<city:
							new_left.append(left[bus_i])
						elif left[bus_i][0]>city:
							new_right.append(left[bus_i])
						else:
							new_mid.append(left[bus_i])
					new_right += right
				elif city >= cities[city_i-1]:
					new_left += left
					for bus_i in range(len(right)):
						if right[bus_i][1]<city:
							new_left.append(right[bus_i])
						elif right[bus_i][0]>city:
							new_right.append(right[bus_i])
						else:
							new_mid.append(right[bus_i])

				for bus_i in range(len(mid)):
					if mid[bus_i][1]<city:
						new_left.append(mid[bus_i])
					elif mid[bus_i][0]>city:
						new_right.append(mid[bus_i])
					else:
						new_mid.append(mid[bus_i])

				re[city_i] = len(new_mid)
				mid = new_mid
				right = new_right
				left = new_left
				city_i +=1
		return re

ous = ""
fo = open("B-large.in",'r')
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
	
fo = open("B-large.out", "w")
fo.write(ous)
fo.close()
