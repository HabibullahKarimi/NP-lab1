#lab1
#In Python, everything that is not in a function, is in the main function
#So I have indicated the start of the main function with a line of ####### 
#Which is around line 44. So it's good to start reading from there.

#importing libraries
import sys
from llist import sllist, sllistnode
import random
import time

#for plotting the graph
import plotly
import plotly.graph_objs



#These are the functions

#generate packet (time of generation and size)
def genPkt(lamda, mu, time):
	intervalTime = random.expovariate(1.0/lamda) 
	arrivalTime = intervalTime + time
	time = arrivalTime 	#update time
	pktSize = int(random.expovariate(1.0/mu)) # in bits

	return [arrivalTime, pktSize, time]

#Finding the time spent in queue
def queue(pktNumber, timeOutPrevious, arrivalTime):
	waitingTime = timeOutPrevious - arrivalTime
	if pktNumber == 1:
		waitingTime = 0
	if waitingTime < 0:
		waitingTime = 0

	return waitingTime

#Pass pkt to the server for service
def server(arrivalTime, waitingTime, pktSize):
	serviceTime = float(pktSize) / serviceRate
	timeIn = arrivalTime + waitingTime
	timeOut = timeIn + serviceTime
	
	return [timeIn, timeOut]

#Adding new node to the linked list, sorted in order of decreasing departure time
def addNode(newNode):
	for i in range(len(lst)):  #Arranges lst 
		if newNode[2] > lst[i][2]:
			node = lst.nodeat(i)
			lst.insertbefore(newNode, node)
			break
	else:
		lst.append(newNode)

#################################################################
# From this below, is the main function

#constants
lamda = 1
mu = 10000  #mean size of packets


#variables
lst = sllist()
time = 0
pktNumber = 0
timeOutPrevious = 0

TotalCustomerInQueue = 0
TotalTimeInQueue = 0
nPacketsInSystem = [0,0,0,0,0,0,0,0,0,0,0]

if len(sys.argv) == 2:	
	if sys.argv[1] == "trace.txt":
		serviceRate = 4000
		loopList = open("trace.txt", "r")
	elif sys.argv[1] == "trace2.txt":
		serviceRate = 7000
		loopList = open("trace2.txt", "r")
	else: 
		six.exit("currently program accepts argv[1] to be trace.txt or trace2.txt\n")
elif len(sys.argv) == 3:
	numberOfpkts = int(sys.argv[1])
	lamda = int(sys.argv[2])
	serviceRate = 10000 #serverice rate is 10Gbps = 10,000 bits/micro second 
	loopList = range(numberOfpkts)
else:
	sys.exit("Wrong number of arguments\n")



npkts = 0

#main loop
for pkt in loopList:
	TotalCustomerInQueue += len(lst)
	pktNumber += 1
	npkts += 1

	#If want to go through 1000 pkts or only, uncomment below 2 lines
	if npkts == 1000:
		break

	if len(sys.argv) == 3:
		getPkt = genPkt(lamda, mu, time)
		arrivalTime = getPkt[0]
		pktSize = getPkt[1]
		time = getPkt[2]
	elif len(sys.argv) == 2:
		line = pkt.split( )
		arrivalTime = float(line[0])
		pktSize = line[1]
	else:
		sys.exit("Program shouldn't reach this line\n")

	waitingTime = queue(pktNumber, timeOutPrevious, arrivalTime)

	pktToServer = server(arrivalTime, waitingTime, pktSize)
	timeIn = pktToServer[0]
	departTime = pktToServer[1]
	timeOutPrevious = departTime

	pkt = [pktNumber,arrivalTime,departTime]

	if len(lst) == 0:
			lst.append(pkt)
			print "[%.3f]: pkt %s arrives and finds %d packets in queue" %(arrivalTime, pktNumber, len(lst))
			continue

	addNode(pkt)
	flag = 0
	for i in range(len(lst)):
		if arrivalTime > lst[i][2]:
			flag = 1
			for j in range(len(lst) - 1, i - 1, -1):
				timeSpent = lst[j][2] - lst[j][1]
				TotalTimeInQueue += timeSpent
				print "[%.3f]: pkt %s departs having spent %.3f us in the system" %(lst[j][2], lst[j][0], timeSpent)
					
			for j in range(len(lst) - 1, i - 1, -1):
				node = lst.nodeat(j)
				lst.remove(node)
				
		if flag == 1:
			break

	if len(lst) <= 10:
		nPacketsInSystem[len(lst)] += 1		

	print "[%.3f]: ppkt %s arrives and finds %d packets in queue" %(arrivalTime, pktNumber, len(lst))

for j in range(len(lst) - 1, - 1, -1):
				timeSpent = lst[j][2] - lst[j][1]
				TotalTimeInQueue += timeSpent
				print "[%.3f]: pkt %s departs having spent %.3f us in the system" %(lst[j][2], lst[j][0], timeSpent)
		

N = TotalCustomerInQueue / npkts
T = float(TotalTimeInQueue) / npkts
print "N = %d, S = %.3f" %(N,T)


probability = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(11):
	probability[i] = float(nPacketsInSystem[i]) / npkts
print nPacketsInSystem
print probability
	
plotly.offline.plot({
"data": [
    plotly.graph_objs.Bar(x=[0,1,2,3,4,5,6,7,8,9,10],y=probability)
]
})

