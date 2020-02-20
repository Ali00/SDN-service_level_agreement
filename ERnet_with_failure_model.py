#Created By Ali Malik 
import zmq
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
#----
import sys
import fnss
import random
import sched
import time
from threading import Thread
import math
import numpy as np
from threading import Timer
from collections import defaultdict
import datetime
from random import randint
import networkx as nx, igraph as ig
import pylab as plt
from collections import Counter
from itertools import tee, izip
import string
import heapq

#-------------------------------------------------------------------------------
#context = zmq.Context()
#socket = context.socket(zmq.REQ)
#socket.connect("tcp://localhost:5556")

net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch, xterms = False )
G = nx.Graph()
Global_Failure_Counter=0  # Global counter to keep the number of all links failure
X_param = 1 # Global counter to avoid the first false failure (division by zero)

def topology():

        global net
        # Add hosts and switches 
        h1 = net.addHost( 'h1', mac= "00:00:00:00:00:01" ) 
        h2 = net.addHost( 'h2', mac= "00:00:00:00:00:02" ) 
        h3 = net.addHost( 'h3', mac= "00:00:00:00:00:03" ) 
        h4 = net.addHost( 'h4', mac= "00:00:00:00:00:04" )
        h5 = net.addHost( 'h5', mac= "00:00:00:00:00:05" ) 
        h6 = net.addHost( 'h6', mac= "00:00:00:00:00:06" ) 
        h7 = net.addHost( 'h7', mac= "00:00:00:00:00:07" ) 
        h8 = net.addHost( 'h8', mac= "00:00:00:00:00:08" )
        h9 = net.addHost( 'h9', mac= "00:00:00:00:00:09" ) 
        h10 = net.addHost( 'h10', mac= "00:00:00:00:00:10" ) 
        h11 = net.addHost( 'h11', mac= "00:00:00:00:00:11" ) 
        h12 = net.addHost( 'h12', mac= "00:00:00:00:00:12" )

        #--------------------------------------------------
        S1 = net.addSwitch( 's1') 
        S2 = net.addSwitch( 's2')  
        S3 = net.addSwitch( 's3')  
        S4 = net.addSwitch( 's4') 
        S5 = net.addSwitch( 's5')  
        S6 = net.addSwitch( 's6')  
        S7 = net.addSwitch( 's7')  
        S8 = net.addSwitch( 's8')  
        S9 = net.addSwitch( 's9')  
        S10 = net.addSwitch( 's10')   
        S11 = net.addSwitch( 's11')  
        S12 = net.addSwitch( 's12')  
        S13 = net.addSwitch( 's13')  
        S14 = net.addSwitch( 's14')  
        S15 = net.addSwitch( 's15')  
        S16 = net.addSwitch( 's16')  
        S17 = net.addSwitch( 's17')  
        S18 = net.addSwitch( 's18')  
        S19 = net.addSwitch( 's19')  
        S20 = net.addSwitch( 's20')  
        S21 = net.addSwitch( 's21')  
        S22 = net.addSwitch( 's22')  
        S23 = net.addSwitch( 's23')  
        S24 = net.addSwitch( 's24')  
        S25 = net.addSwitch( 's25')  
        S26 = net.addSwitch( 's26')  
        S27 = net.addSwitch( 's27')  
        S28 = net.addSwitch( 's28')  
        S29 = net.addSwitch( 's29')  
        S30 = net.addSwitch( 's30')  
        S31 = net.addSwitch( 's31')  
        S32 = net.addSwitch( 's32')  
        S33 = net.addSwitch( 's33')  
        S34 = net.addSwitch( 's34')  
        S35 = net.addSwitch( 's35')  
        S36 = net.addSwitch( 's36') 
        S37 = net.addSwitch( 's37')  
        c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )

        # Adding links
        net.addLink(h1, S18)  #Source P1 (Gold)
        net.addLink(h2, S30)  #Destination P1 (Gold)
        net.addLink(h3, S11)  #Source P2 (Gold)
        net.addLink(h4, S20)  #Destination P2 (Gold)
        net.addLink(h5, S21)  #Source P3 (Gold)
        net.addLink(h6, S3)   #Destination P3 (Gold)

        net.addLink(h7, S18)  #Source P1 (Bronz)
        net.addLink(h8, S30)  #Destination P1 (Bronz)
        net.addLink(h9, S11)  #Source P2 (Bronz)
        net.addLink(h10, S20)  #Destination P2 (Bronz)
        net.addLink(h11, S21)  #Source P3 (Bronz)
        net.addLink(h12, S3)  #Destination P3 (Bronz)



        #10
        net.addLink( S1 , S27 ) 
        net.addLink( S1 , S2 )         
        net.addLink( S1 , S3 ) 
        net.addLink( S2 , S20 ) 
        net.addLink( S2 , S21 ) 
        net.addLink( S2 , S23 ) 
        net.addLink( S3 , S23 ) 
        net.addLink( S3 , S12 ) 
        net.addLink( S3 , S13 ) 
        net.addLink( S3 , S17 ) 
 
        #20 
        net.addLink( S4 , S16 ) 
        net.addLink( S4 , S36 ) 
        net.addLink( S5 , S8 ) 
        net.addLink( S5 , S30 ) 
        net.addLink( S5 , S14 ) 
        net.addLink( S6 , S33 ) 
        net.addLink( S6 , S18 ) 
        net.addLink( S6 , S35 ) 
        net.addLink( S7 , S8 ) 
        net.addLink( S7 , S9 ) 
        net.addLink( S7 , S29 ) 
 
        #30 
        net.addLink( S8 , S26 ) 
        net.addLink( S8 , S21 ) 
        net.addLink( S9 , S24 ) 
        net.addLink( S9 , S32 ) 
        net.addLink( S9 , S10 ) 
        net.addLink( S10 , S11 ) 
        net.addLink( S10 , S36 ) 
        net.addLink( S10 , S29 ) 
        net.addLink( S10 , S37 ) 
        net.addLink( S11 , S24 ) 
 
        #40 
        net.addLink( S11 , S35 ) 
        net.addLink( S12 , S33 ) 
        net.addLink( S12 , S34 ) 
        net.addLink( S12 , S18 ) 
        net.addLink( S12 , S35 ) 
        net.addLink( S13 , S19 ) 
        net.addLink( S13 , S35 ) 
        net.addLink( S14 , S21 ) 
        net.addLink( S15 , S25 ) 
        net.addLink( S15 , S26 ) 
 
        #50 
        net.addLink( S15 , S29 ) 
        net.addLink( S16 , S37 ) 
        net.addLink( S16 , S22 ) 
        net.addLink( S17 , S24 ) 
        net.addLink( S17 , S27 ) 
        net.addLink( S19 , S24 ) 
        net.addLink( S20 , S28 ) 
        net.addLink( S20 , S31 ) 
        net.addLink( S21 , S32 ) 
        net.addLink( S22 , S36 ) 
 
        #57 
        net.addLink( S23 , S28 ) 
        net.addLink( S25 , S37 ) 
        net.addLink( S26 , S30 ) 
        net.addLink( S27 , S32 ) 
        net.addLink( S28 , S34 ) 
        net.addLink( S31 , S34 ) 
        

        # Build The Network 
        net.build()
        c0.start()
        S1.start(  [c0] )
        S2.start(  [c0] )
        S3.start(  [c0] )
        S4.start(  [c0] )
        S5.start(  [c0] ) 
        S6.start(  [c0] )
        S7.start(  [c0] )
        S8.start(  [c0] )
        S9.start(  [c0] )
        S10.start(  [c0] ) 
        S11.start(  [c0] )
        S12.start(  [c0] )
        S13.start(  [c0] )
        S14.start(  [c0] )
        S15.start(  [c0] ) 
        S16.start(  [c0] )
        S17.start(  [c0] )
        S18.start(  [c0] )
        S19.start(  [c0] )
        S20.start(  [c0] )   
        S21.start(  [c0] )
        S22.start(  [c0] )
        S23.start(  [c0] )
        S24.start(  [c0] )
        S25.start(  [c0] ) 
        S26.start(  [c0] )
        S27.start(  [c0] )
        S28.start(  [c0] )
        S29.start(  [c0] )
        S30.start(  [c0] )   
        S31.start(  [c0] )
        S32.start(  [c0] )
        S33.start(  [c0] )
        S34.start(  [c0] )
        S35.start(  [c0] ) 
        S36.start(  [c0] )
        S37.start(  [c0] ) 
        
        ############################################
        h1.cmd("arp -s 10.0.0.2 00:00:00:00:00:02")
        h2.cmd("arp -s 10.0.0.1 00:00:00:00:00:01") 
        h3.cmd("arp -s 10.0.0.4 00:00:00:00:00:04")
        h4.cmd("arp -s 10.0.0.3 00:00:00:00:00:03")  
        h5.cmd("arp -s 10.0.0.6 00:00:00:00:00:06")
        h6.cmd("arp -s 10.0.0.5 00:00:00:00:00:05")  
        h7.cmd("arp -s 10.0.0.8 00:00:00:00:00:08")
        h8.cmd("arp -s 10.0.0.7 00:00:00:00:00:07")  
        h9.cmd("arp -s 10.0.0.10 00:00:00:00:00:10")
        h10.cmd("arp -s 10.0.0.9 00:00:00:00:00:09")  
        h11.cmd("arp -s 10.0.0.12 00:00:00:00:00:12")
        h12.cmd("arp -s 10.0.0.11 00:00:00:00:00:11")  
        #net.cmd("xterm h1")
        #############################################
        print "*** Running CLI"
        CLI( net )

        #print "*** Stopping network"
        #net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
    #Topology Graph
    G.add_edges_from([(1, 27), (1, 2), (1, 3), (2, 20), (2, 21), (2, 23), (3, 23), (3, 12), (3, 13), (3, 17), (4, 16), (4, 36), (5, 8),  (5, 30), (5, 14), (6, 33), (6, 18), (6, 35), (7, 8), (7, 9), (7, 29), (8, 26), (8, 21), (9, 24), (9, 32), (9, 10), (10, 11), (10, 36), (10, 29), (10, 37), (11, 24), (11, 35), (12, 33), (12, 34), (12, 18), (12, 35), (13, 19), (13, 35), (14, 21), (15, 25), (15, 26), (15, 29), (16, 37), (16, 22), (17, 24), (17, 27), (19, 24), (20, 28), (20, 31), (21, 32), (22, 36), (23, 28), (25, 37), (26, 30), (27, 32), (28, 34), (31, 34)])
    Nodes= nx.nodes(G)
    Edges= nx.edges(G)
    print 'The nodes are', Nodes
    print 'The edges are', Edges

    #Dictionary of switches to return --> e.g.  Link (1,2) --> (s1, s2)
    Switches_Dictionary = { (1): 's1', (2): 's2', (3): 's3',(4): 's4', (5): 's5', (6): 's6',
                           (7): 's7', (8): 's8', (9): 's9', (10): 's10', (11): 's11', (12): 's12', (13): 's13', (14): 's14',
                           (15): 's15', (16): 's16', (17): 's17', (18): 's18', (18): 's18', (19): 's19', (20): 's20', (21): 's21',
                           (22): 's22', (23): 's23', (24): 's24', (25): 's25', (26): 's26', (27): 's27', (28): 's28', (29): 's29',
                           (30): 's30', (31): 's31' , (32): 's32', (33): 's33', (34): 's34', (35): 's35', (36): 's36', (37): 's37'}
    #Link's Length Dictionary
    Links_Lengths_Dictionary = {(1, 27) :334.44, (1, 2) : 419.81 , (1, 3) : 391.20 , (2, 20) : 598.60 , (2, 21) : 1152.38 , (2, 23) : 174.94 , (3, 23) : 499.44 , (3, 12) : 342.74 , (3, 13) : 263.72 , (3, 17) : 396.71 , (4, 16) : 787.45 , (4, 36) : 483.52 , (5, 8) : 1081.53 ,  (5, 30) : 526.12 , (5, 14) : 908.16 , (6, 33) : 406.33 , (6, 18) : 308.81 , (6, 35) : 710.63 , (7, 8) : 267.91 , (7, 9) : 355.41 , (7, 29) : 252.56 , (8, 26) : 367.61 , (8, 21) : 518.02 , (9, 24) : 304.30 , (9, 32) : 348.76 , (9, 10) : 504.50 , (10, 11) : 255.71 , (10, 36) : 354.79 , (10, 29) : 279.76 , (10, 37) : 516.42 , (11, 24) : 393.30 , (11, 35) : 365.89 , (12, 33) : 163.04 , (12, 34) : 1585.78 , (12, 18) : 463.97 , (12, 35) : 357.29 , (13, 19) : 174.38 , (13, 35) : 173.83 , (14, 21) : 426.19 , (15, 25) : 291.62 , (15, 26) : 317.74 , (15, 29) : 444.22 , (16, 37) : 914.78 , (16, 22) : 395.92 , (17, 24) : 182.92 , (17, 27) : 147.36 , (19, 24) : 182.61 , (20, 28) : 504.93 , (20, 31) : 830.64 , (21, 32) : 477.97 , (22, 36) : 522.27 , (23, 28) : 553.72 , (25, 37) : 253.87 , (26, 30) : 329.29 , (27, 32) : 217.65 , (28, 34) : 503.11 , (31, 34) : 311.84 }


    print 'The minimum Length in the dictionary is:'
    print Links_Lengths_Dictionary[min(Links_Lengths_Dictionary, key=lambda k: Links_Lengths_Dictionary[k])]
    #-------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------

    #generate the gamma parameter for all the links in the network topology

    Gama = []

    #for i in range (len(Edges)):

        #Gama.append(random.uniform(0.01, 0.05))

    x = len(Edges)

    Gama = np.random.uniform(0.002, 0.006, x)

    print 'The links Gama is :\n', Gama

    #-------------------------------------------------------------------------------------------------------------

    print 'The minimum Length in the dictionary is:'

    print Links_Lengths_Dictionary[min(Links_Lengths_Dictionary, key=lambda k: Links_Lengths_Dictionary[k])]

    #-------------------------------------------------------------------------------------------------------------

    #Now, We will compute the MTBF value of each link in this topology...

    #Through the formuls -->  MTBF_link[i]= (CC_link[i]*365*24)/Lenght of link[i],      where CC=Cable_Cut

    minimum = Links_Lengths_Dictionary[min(Links_Lengths_Dictionary, key=lambda k: Links_Lengths_Dictionary[k])]

    cc=[]

    for i in range (len(Edges)):

       cc.append((Links_Lengths_Dictionary[Edges[i]] / minimum))

    print "The cable cut per year \n", cc

    #-------------------------------------------------------------------------------------------------------------

    MTBF=[]

    for i in range (len(Edges)):

        MTBF.append((cc[i]*365*24)/Links_Lengths_Dictionary[Edges[i]])

    print "The MTBF of each link: \n", MTBF

    #-------------------------------------------------------------------------------------------------------------

    MTTR=[]

    Length_Sum=0

    #for i in range (len(Edges)):

        #Length_Sum= Length_Sum + Links_Lengths_Dictionary[Edges[i]]

    #print 'The Total length is :', Length_Sum

    for i in range (len(Edges)):

        #MTTR.append (round(float(Links_Lengths_Dictionary[Edges[i]]) / (float (Length_Sum)) *100))

        #MTTR.append (float(Links_Lengths_Dictionary[Edges[i]]) / (float (Length_Sum))) # stopped currently

        mttr = (round(Links_Lengths_Dictionary[Edges[i]] * Gama[i]))

        if mttr < 1:

           mttr = 1

        MTTR.append (mttr)

        #MTTR.append (round(Links_Lengths_Dictionary[Edges[i]] * Gama[i]))

    print "The MTTR of each link: \n", MTTR

    #-------------------------------------------------------------------------------------------------------------

    class PriorityQueue:

          def __init__(self):

              self._queue = []

              self._index = 0



          def push(self, item, priority):

              heapq.heappush(self._queue, (priority, self._index, item)) # (-priority) for highest first

              self._index += 1



          def pop(self):

              return heapq.heappop(self._queue)[-1]

          def isEmpty(self):

              return self._queue == []



          def size(self):

              return len(self._queue)

    #--------------------------------------------------------------------------------------------------------------

    q = PriorityQueue() # Object of priorityQueue class

    #--------------------------------------------------------------------------------------------------------------



    #Implement the Links to define network links with different parameters

    class Links(object):



          def __init__(self, ID=None, Name=None, Length=None, MTBF=None, MTTR=None, Next_Failure=None,  F_Count=None, P_Failure=None,  Link_state=None):

              self.ID = ID                      # Link's ID e.g. (node1, node2)

              self.Name = Name                  # Link's name (e.g. 0 , 1, etc.)

              self.Length = Length              # Link's length

              self.MTBF = MTBF                  # Mean Time Between Failure

              self.MTTR = MTTR                  # Mean Time To Recover

              self.Next_Failure = Next_Failure  # Time To failure event

              self.F_Count= F_Count             # Lcal Counter of link failure

              self.P_Failure= P_Failure         #Links_ Probability of link failure

              self.Link_state = Link_state      # Boolean indicator to indicate whether link down/up

    #------------------------------------------------------------------------------



    L=[] # List that contains a set of links as a class objects

    for i in range (len(Edges)): # To initailize the link objects

        L.append((Links(Edges[i], i , Links_Lengths_Dictionary[Edges[i]], MTBF[i], MTTR[i], 0, 0, 0, True)))



    for i in range (len(Edges)): # Generate the initial "Next_Failure" for all links

        TTF= np.random.exponential(scale=L[i].MTBF, size=1) # Exponential Distribution[Mean= MTBF of current link]

        L[i].Next_Failure = round(TTF) + 1 # To avoid zeros at the begining, we add (+1) to the TTF



    for i in range (len(Edges)):

        print "Link %s that named % s with Length %s and MTBF equals to %s and MTTR %s and Next_Failure is %s and Failure counter equals to %s and failure probability equals to %s and the Link_state is %s" % (L[i].ID, L[i].Name, L[i].Length, L[i].MTBF, L[i].MTTR, L[i].Next_Failure, L[i].F_Count, L[i].P_Failure, L[i].Link_state)





    for i in range (len(Edges)):

        q.push(L[i].Name, L[i].Next_Failure)



    print 'Test Q size', q.size()

    #------------------------------------------------------------------------------

    #Schedular and it's related functions

    scheduler = sched.scheduler(time.time, time.sleep)

    now = datetime.datetime.now()

    #------------------------------------------------------------------------------

    def push(link_return):

        global net



        if (L[link_return].Link_state == False):

           L[link_return].Link_state = True

           print 'The Link', L[link_return].ID, 'with Next_Failure =', L[link_return].Next_Failure ,'will be returened'

           TTF2= np.random.exponential(scale=L[link_return].MTBF, size=1)

           if TTF2 == 0:    # To avoid zeros
              TTF2 =1

           L[link_return].Next_Failure = round(TTF2)

           switches_R = L[link_return].ID

           switch1 = Switches_Dictionary [switches_R[0]]

           switch2 = Switches_Dictionary [switches_R[1]]

           net.configLinkStatus(switch1, switch2,'up')

           print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'

           print 'The repaired link is ', switch1, '--', switch2

           print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'

           q.push(L[link_return].Name, L[link_return].Next_Failure)

           print 'The new Next_Failure of link', L[link_return].ID, 'is :', round(TTF2)

        else:

             print 'The link', L[link_return].ID ,'will be returened'

             TTF2= np.random.exponential(scale=L[link_return].MTBF, size=1)

             if TTF2 == 0:    # To avoid zeros
                TTF2 =1

             L[link_return].Next_Failure = round(TTF2)

             q.push(L[link_return].Name, L[link_return].Next_Failure)

             print 'The new Next_Failure of link', L[link_return].ID, 'is :', round(TTF2)



    #------------------------------------------------------------------------------

    def Send_To_Controller(lnk, lnk_prob):

        context = zmq.Context()

        socket = context.socket(zmq.REQ)

        #global socket

        socket.connect("tcp://localhost:5556")

        x = str(lnk)
        y= float(lnk_prob)

        #LinkPrediction = {"type": "LinkFailure", "link": x}
        LinkPrediction = {"type": "LinkFailure", "link": x, "probability": y}

        #send command of failure link event

        socket.send_json(LinkPrediction)

        #For every time you use a send method you need to run the receive method

        resp = socket.recv_json()

        # close the socket when you're done

        socket.close()

    #------------------------------------------------------------------------------

    def schedule(link):

        global net

        print time.time()



        if (L[link].Link_state == False):

          print 'The link', L[link].ID, ' poped out with Next_Failure =', L[link].Next_Failure

          switches_F = L[link].ID

          switch1 = Switches_Dictionary [switches_F[0]]

          switch2 = Switches_Dictionary [switches_F[1]]

          net.configLinkStatus(switch1, switch2,'down')

          print '********************************************'

          print 'The failed link is ', switch1, '--', switch2

          print '********************************************'

          mu = (math.log(L[link].MTTR) - ((0.5) * math.log(1 + ((0.6 * L[link].MTTR)**2 / L[link].MTTR**2))))

          sig = math.sqrt((math.log (1 + ((0.6 * L[link].MTTR)**2 / L[link].MTTR**2))))

          Log_Normal = np.random.lognormal(mu, sig, 1) #Lognormal #distribution for the next Time To Recover event

          print 'The link', L[link].ID, 'will wait up to', round(Log_Normal), 'to get recovery'

          scheduler.enter(round(Log_Normal)*60, 1, push, (L[link].Name,))

          get_out() #calling the function to schedule the next link failure

          scheduler.run()

        else:

           print 'The link', L[link].ID ,'will not wait and directly returned to the Q with a new Next_Time _To_Failure'

           scheduler.enter(2, 1, push, (L[link].Name,))

           get_out() #calling the function to schedule the next link failure

           scheduler.run()

    #------------------------------------------------------------------------------

    def get_out():

        global Global_Failure_Counter

        global X_param

        #csv1 = open(TP, "a")


        if q.isEmpty() != True:

           F_Flag = True  #indicator

           x = q.pop()

           Dicision_F = random.randint(0, 1) # To decide if the link is gonna faile or not

           if Dicision_F == 1:               # Means the link is gonna fail in reality

              X_param+=1

              F_Flag = False

              L[x].Link_state = False      # Change link state to false as an indicator

              L[x].F_Count+=1              # Increment the failure counter of the current link

              Global_Failure_Counter+= 1   # Increment the global failure counter

              k = L[x].ID
              print "The link that will fail and put in TP file is :", k
              #row1 = "\"" + str(k) + "\"" + "," + "TP_FN" +"\n"
              #csv1.write(row1)
              #csv1.close()
              

           if (Dicision_F == 0) and (X_param == 1): # Means the link is not gonna fail in reality, but since it is the first case

                                                    # hence, we consider it as a real failure to avoid the division by zero error

              X_param+=1

              F_Flag = False

              L[x].Link_state = False      # Change link state to false as an indicator

              L[x].F_Count+=1              # Increment the failure counter of the current link

              Global_Failure_Counter+= 1   # Increment the global failure counter
              
              k = L[x].ID
              print "The link that will fail and put in TP file is :", k
              #row1 = "\"" + str(k) + "\"" + "," + "TP_FN" +"\n"
              #csv1.write(row1)
              #csv1.close()


           L[x].P_Failure = (float(L[x].F_Count) / float(Global_Failure_Counter)) * 100

           print 'Link ', L[x].ID , 'will pop out from the Q with Next time to failure =', L[x].Next_Failure

           print 'The probability of failure to the link', L[x].ID, 'is ', L[x].P_Failure, '%'

           if Dicision_F == 1:

              print "The failed link and its probability will be sent to the controller"
              scheduler.enter(5, 1, Send_To_Controller, (L[x].ID, L[x].P_Failure,)) #send updates to the controller 

           #if (L[x].P_Failure > 0):  #The threshold condition is greater than 0%

                    #print 'The link', L[x].ID, 'Has a failure probability over the threshould'

                    #Dicision = random.randint(0, 1)

                    #if Dicision == 1 :  #Means the controller will receive a notification and its a true positive

                           #if ((L[x].Next_Failure) > 2):

                              #wt = (L[x].Next_Failure) - 2

                              #print 'The controller will receive a notification after', wt, 'mins'

                              #scheduler.enter(wt*60, 1, Send_To_Controller, (L[x].ID,)) #send a notification

                                                #about the link who will fail after two mins (i.e. wt * 60)

                           #else:

                                  #print 'There is no enough time to send a notification to the controller, sorry'

                                  #scheduler.enter(2, 1, Send_To_Controller, (L[x].ID, L[x].P_Failure,)) #send a notification 

           #else:

                #print 'The link', L[x].ID, 'Has a failure probability below the threshould'

           scheduler.enter((L[x].Next_Failure)*60, 1, schedule, (L[x].Name,)) # Next_Failure *60 --> in minutes



        else:

               print 'The Q is empty ... '

        scheduler.run() #running the schedular
        

    #------------------------------------------------------------------------------

    print '**************************************'

    print 'START TIME:', time.time(), '-->', now

    print '**************************************'

    time.sleep(120) # Wait up to 2 mins then start the event failure simulation

    get_out()


