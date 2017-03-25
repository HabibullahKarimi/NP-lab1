#lab1
#In Python, everything that is not in a function, is in the main function
#So I have indicated the start of the main function with a line of ####### 
#Which is around line 44. So it's good to start reading from there.

#importing libraries
import sys
from llist import sllist, sllistnode
import random
import time



#These are the functions

#generate packet (time of generation and size)
def genPkt(lamda, mu, time):
	intervalTime = random.expovariate(1.0/lamda) 
	arrivalTime = intervalTime + time
	time = arrivalTime + time 	#update time
	pktSize = int(random.expovariate(1.0/mu)) # in bits
	#print "Arrival time in us is: %s and pktsize is: %s" %(arrivalTime, pktSize)
	print "intervalTime is %s" %(intervalTime)
	return [arrivalTime, pktSize, time]

def queue(pktNumber, timeOutPrevious, arrivalTime):
	waitingTime = timeOutPrevious - arrivalTime
	#print "arrival time of new pkt is %s dep time of prev pkt is %s" %(arrivalTime, timeOutPrevious)
	#print "waitingTime1 is %s" %(waitingTime)
	if pktNumber == 1:
		waitingTime = 0
	if waitingTime < 0:
		waitingTime = 0

	#print "waitingTime is %s" %(waitingTime)
	return waitingTime

#Pass pkt to the server for service
def server(arrivalTime, waitingTime, pktSize):
	serviceTime = float(pktSize) / serviceRate
	print "Service time is %s" %(serviceTime) 
	timeIn = arrivalTime + waitingTime
	timeOut = timeIn + serviceTime
	
	#print "Departure time is %s" %(timeOut)
	return [timeIn, timeOut]

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
npkts = 10
lamda = 1
mu = 10000  #mean size of packets
serviceRate = 10000 #serverice rate is 10Gbps = 10,000 bits/micro second 
eventTypeOne = 0
eventTypeTwo = 1

#variables
npkts = int(sys.argv[1])
lamda = int(sys.argv[2])

lst = sllist()
time = 0
pktNumber = 0
timeOutPrevious = 0

#main loop
for pkt in range(npkts):
	pktNumber += 1
	print "\n"
	getPkt = genPkt(lamda, mu, time)
	arrivalTime = getPkt[0]
	print "arrivaltime1 %s" %(arrivalTime)
	pktSize = getPkt[1]
	time = getPkt[2]
	#print lst
	#print "prev out is: %s arrival time is %s" %(timeOutPrevious, arrivalTime)
	waitingTime = queue(pktNumber, timeOutPrevious, arrivalTime)
	print "waiting time is %s" %(waitingTime)
	#print "waiting time is %s" %(waitingTime)

	pktToServer = server(arrivalTime, waitingTime, pktSize)
	timeIn = pktToServer[0]
	departTime = pktToServer[1]
	timeOutPrevious = departTime

	pkt = [pktNumber,arrivalTime,departTime]

	
	if len(lst) == 0:
			lst.append(pkt)
			print "***[%s]: pkt %s arrives and finds %s packets in queue" %(arrivalTime, pktNumber, len(lst))
			continue

	addNode(pkt)
	print lst
	flag = 0
	for i in range(len(lst)):
		if arrivalTime > lst[i][2]:
			flag = 1
			for j in range(len(lst) - 1, i - 1, -1):
				timeSpent = lst[j][2] - lst[j][1]
				print "---[%s]: pkt %s departs having spent %s us in the system" %(lst[j][2], lst[j][0], timeSpent)
					
			for j in range(len(lst) - 1, i - 1, -1):
				node = lst.nodeat(j)
				lst.remove(node)
				
		if flag == 1:
			break

	print "---[%s]: ppkt %s arrives and finds %s packets in queue" %(arrivalTime, pktNumber, len(lst))

	


		




