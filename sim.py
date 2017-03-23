#lab1
import sys
from llist import sllist, sllistnode
import random
import time






#generate packet (time of generation and size)
def genPkt(lamda, mu, time):
	intervalTime = random.expovariate(1.0/lamda) 
	arrivalTime = intervalTime + time
	time = arrivalTime + time 	#update time
	pktSize = int(random.expovariate(1.0/mu)) # in bits
	return [arrivalTime, pktSize, time]

def queue(pktnumber, timeOutPrevious, arrivalTime):
	if (pktnumber == 1):
		waitingTime = 0
	elif (timeOutPrevious > arrivalTime):
		waitingTime = timeOutPrevious - arrivalTime
	else:
		waitingTime = 0

	return waitingTime

#Pass pkt to the server for service
def server(arrivalTime, waitingTime, pktSize):
	serviceTime = pktSize / serviceRate
	timeIn = arrivalTime + waitingTime
	timeOut = timeIn + serviceTime
	
	return [timeIn, timeOut]




# From this below, is the main function

#constants
npkts = 10
lamda = 1
mu = 10000  #mean size of packets
serviceRate = 10000 #serverice rate is 10Gbps = 10,000 bits/micro second 

#variables
npkts = sys.argv[1]
lamda = sys.argv[2]

pkts = sllist()

time = 0
pktnumber = 0
timeOutPrevious = 0

#main loop
for pkt in range(npkts):
	getPkt = genPkt(lamda, mu, time)
	arrivalTime = getPkt[0]
	pktSize = getPkt[1]
	time = getPkt[2]

	waitingTime = queue(pktnumber, timeOutPrevious, arrivalTime)

	pktToServer = server(arrivalTime, waitingTime, pktSize)
	timeIn = pktToServer[0]
	timeOut = pktToServer[1]
	timeOutPrevious = timeOut

	pktnumber += 1












i = 0
while i <= npkts


	





#Event management library
def addNewEvent():

def deleteEvent():

def retrieveNextEvent():




#Source model








#Service model'''

