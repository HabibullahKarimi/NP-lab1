from llist import sllist, sllistnode

i = 0
lst = sllist()
lst.append([0,0,0])
print lst[0][2]
def addNode(depTime, newNode):
	for i in range(len(lst)):  #Arranges lst 
		if depTime > lst[i][2]:
			node = lst.nodeat(i)
			lst.insertbefore(newNode, node)
			break
	else:
		lst.append(newNode)

node = [1,1,1]
depTime = 3
addNode(depTime, node)

print lst

node = [3,3,3]
depTime = 5
addNode(depTime, node)

node = [1.5,1.5,1.5]
depTime = -1
addNode(depTime, node)
print lst