# 90 Mins Same as Small
class Solution:
	def main(self,maze):
		S = len(maze)
		dic = {}
		for i in range(S):
			for j in range(S):
				dic[int(maze[i][j])]=(i,j)
		r = 1
		d = 1
		cur = 1
		S2 = S*S
		new_r = 1
		new_d = 1
		while cur < S2:
			isNeig_UD = (dic[cur][0] == dic[cur+1][0]+1) or (dic[cur][0] == dic[cur+1][0]-1)
			isNeig_UD = isNeig_UD and (dic[cur][1] == dic[cur+1][1])

			isNeig_LR = (dic[cur][1] == dic[cur+1][1]+1) or (dic[cur][1] == dic[cur+1][1]-1)
			isNeig_LR = isNeig_LR and (dic[cur][0] == dic[cur+1][0])

			if isNeig_UD or isNeig_LR:
				new_d +=1
				# print cur,r,new_d
			else:
				if new_d > d:
					r = new_r
					d = new_d
				# print cur,r,d
					
				new_r = cur+1
				new_d = 1
			
			cur +=1

			if new_d > d:
				r = new_r
				d = new_d

		return (r,d)

ous = ""
fo = open("A-large-practice.in", "r")
# fo = open("input",'r')
ins = fo.read()
ins = ins.splitlines()
fo.close()
Case_num = int(ins[0])
line = 2

for cn in range(Case_num):
	S = int(ins[line])
	line+=1

	maze = []
	for i in range(S):
		maze.append(ins[line+i].split())

	line+=S
	# for i in maze:
	# 	print i

	ous +="Case #"+str(cn+1)+": "
	s = Solution()
	(r,d)=s.main(maze)
	ous += ' '+str(r)+' '+str(d)
	ous += '\n'

	# line +=1
	
fo = open("A-large.out", "w")
fo.write(ous)
fo.close()

