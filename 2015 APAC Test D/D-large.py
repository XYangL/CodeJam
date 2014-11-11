# Same as small; 2 hours;
# Understanding P cost a lot time
class Solution:
	def __init__(self,pos_dic):
		self.kind_dic ={}
		self.kind_dic['K'] = ([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1],1)
		self.kind_dic['Q'] = ([-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1],7)
		self.kind_dic['R'] = ([-1,1,0,0],[0,0,-1,1],7)
		self.kind_dic['B'] = ([-1,1,-1,1],[-1,1,1,-1],7)
		self.kind_dic['N'] = ([2,2,-2,-2,1,1,-1,-1],[1,-1,1,-1,2,-2,2,-2],1)
		self.kind_dic['P'] = ([-1,1],[1,1],1)#!!!
		self.re = 0

		self.pos_dic = pos_dic
		self.board = []
		self.initBoard()
	
	def initBoard(self):
		self.board = []
		for j in range(8):
			self.board.append([0]*8)

		for po in self.pos_dic.keys():
			self.board[int(po[1])-1][ord(po[0])-ord('A')]=self.pos_dic[po]
		
		# for line in self.board:
		# 	print line
		# print '\n'

	def is_vald(self,i,j):
		if i>-1 and i <8 and j > -1 and j <8:
			return True
		else:
			return False

	def main(self):
		for po in self.pos_dic.keys():#'A1'='K'
			start_i = int(po[1])-1
			start_j = ord(po[0])-ord('A')
			kind = self.pos_dic[po]
			move_num = len(self.kind_dic[kind][0])
			move_i = self.kind_dic[kind][0]
			move_j = self.kind_dic[kind][1]
			move_most_place = self.kind_dic[kind][2]

			if move_most_place == 1:
				for index in range(move_num):
					next_i = start_i+move_i[index]
					next_j = start_j+move_j[index]
					if self.is_vald(next_i,next_j) and self.board[next_i][next_j]!= 0:
						self.re +=1
						# print kind,start_i,start_j,next_i,next_j	

			elif move_most_place == 7:
				for index in range(move_num):
					for place in range(1,8): #!!!
						next_i = start_i+move_i[index]*place
						next_j = start_j+move_j[index]*place
						if self.is_vald(next_i,next_j) and self.board[next_i][next_j]!= 0:
							self.re +=1
							# print kind,start_i,start_j,next_i,next_j	
							break
			# else: # P !!!
			# 	for place in range(1,8):
			# 		next_i = start_i+place
			# 		next_j = start_j+place
				
			# 		if self.is_vald(next_i,next_j) and self.board[next_i][next_j]!= 0:
			# 				print kind,start_i,start_j,next_i,next_j
			# 				self.re +=1
		return self.re


ous = ""
fo = open("D-large-practice.in", "r")
# fo = open("input", "r")
lines = fo.read().splitlines()
fo.close()
T = int(lines[0])
index = 1
for caseNum in range(T):
	N = int(lines[index])
	index +=1

	ins = lines[index:index+N]
	# print ins,'\n'
	index += N
	
	pos_dic = {}
	for i in ins:
		pos_dic[i[0:2]]=i[3]
	# if caseNum+1 == 12:
	# 	print pos_dic,'\n-----\n'
	
	ous +="Case #"+str(caseNum+1)+": "
	s = Solution(pos_dic)
	ous += str(s.main())
	ous += '\n'
	
fo = open("D-large.out", "w")
fo.write(ous)
fo.close()
