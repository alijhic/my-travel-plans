

def findlast(txxt,target):
	current_loc=-1
	last = current_loc
	while txxt.find(target,current_loc+1)>-1:
		#last=len(target)-1+txxt.find(target,current_loc+1)
		last=txxt.find(target,current_loc+1)
		current_loc=last


	return last

print findlast("baba moma lala baba kaka sasa fafa baba kaka lala","baba")
print findlast("baba moma lala baba kaka sasa fafa baba kaka lala","haha")
print findlast("jojo baba moma lala baba kaka sasa fafa baba kaka lala","jojo")

