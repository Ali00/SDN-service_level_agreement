#------------------------------------------
import pox.lib.packet as pkt
import zmq  # Here we get ZeroMQ
import threading
import thread
import sys
from collections import deque  # Standard python queue structure
import json
import ast
import decimal
from fastnumbers import fast_real
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.recoco import Timer
from collections import defaultdict
from pox.openflow.discovery import Discovery
from pox.lib.util import dpid_to_str
import time
import datetime
#from datetime import datetime
from itertools import tee, izip
from matplotlib import pylab
from pylab import *
import igraph
from igraph import *
import numpy as np
import networkx as nx, igraph as ig
from random import randint
from collections import defaultdict
from itertools import tee, izip
import fnss
from fnss.units import capacity_units, time_units
import fnss.util as util
import sched
from threading import Timer
import collections
#calling disjoint path algorithm fuction as follows:
from disjoint_paths import edge_disjoint_shortest_pair
#------------------------------------------
#from matplotlib import pylab 
#from pylab import * 
#import igraph 
#from igraph import * 
#import numpy as np 
#import networkx as nx, igraph as ig 
#from random import randint 
#from collections import defaultdict 
#from itertools import tee, izip 
#------------------------------------------
#from pox.core import core
#import pox.openflow.libopenflow_01 as of
#from pox.lib.revent import *
#from pox.lib.recoco import Timer
#from collections import defaultdict
#from pox.openflow.discovery import Discovery
#from pox.lib.util import dpid_to_str
#import time
import copy
#-----------------------------------------
P1_G = 0
P2_G = 0
P3_G = 0
P1_S = 0
P2_S = 0
P3_S = 0
#-----------------------------------------
log = core.getLogger()
mac_map = {}
switches = {}
myswitches=[]
adjacency = defaultdict(lambda:defaultdict(lambda:None))
current_p=[]
G = nx.Graph()  #initiate the graph G to maintain the network topology
counter = 1
#---------------------------------------------------------
#The new added stuff
#---------------------------------------------------------
# Setup the ZeroMQ endpoint URL.
PUB_URL = "tcp://*:5555"  # Used for publishing information
REQ_URL = "tcp://*:5556"  # Used to receive requests
#--------
F_SET =[]       # Failure set that holds the failed links
Failure_events = "Recorded_Events.csv"  # Excel file to store the failure events
#---------------------------------------------------------------------------------------------------
#Hops_after_events = "my_hops.csv" #To store the number of hops after failure events
Gold_Hops_P1 = "Golden_Service_Path1.csv"  # Excel file to store the Golden service hops of path1
Silver_Hops_P1 = "Silver_Service_Path1.csv"  # Excel file to store the Silver service hops of path1
#---------------------------------------------------------------------------------------------------
Gold_Hops_P2 = "Golden_Service_Path2.csv"  # Excel file to store the Golden service hops of path2
Silver_Hops_P2 = "Silver_Service_Path2.csv"  # Excel file to store the Silver service hops of path2
#---------------------------------------------------------------------------------------------------
Gold_Hops_P3 = "Golden_Service_Path3.csv"  # Excel file to store the Golden service hops of path3
Silver_Hops_P3 = "Silver_Service_Path3.csv"  # Excel file to store the Silver service hops of path3
#---------------------------------------------------------------------------------------------------
csv1 = open(Failure_events, "a") 
#---------------------------------------------------------------------------------------------------
csv2 = open(Gold_Hops_P1, "a") 
csv3 = open(Silver_Hops_P1, "a") 
#---------------------------------------------------------------------------------------------------
csv4 = open(Gold_Hops_P2, "a") 
csv5 = open(Silver_Hops_P2, "a") 
#---------------------------------------------------------------------------------------------------
csv6 = open(Gold_Hops_P3, "a") 
csv7 = open(Silver_Hops_P3, "a") 
#---------------------------------------------------------------------------------------------------

columnTitle1 = "Failed-Link && Time\n" 
csv1.write(columnTitle1)
#---------------------------------------------------------------------------------------------------
columnTitle2 = "New-Golden-Path && No.hops && Time \n"  # To record the Gold service hops
csv2.write(columnTitle2)
#---------------------------------------------------------------------------------------------------
columnTitle3 = "New-Silver-Path && No.hops && Time \n"  # To record the Silver service hops
csv3.write(columnTitle3)
#---------------------------------------------------------------------------------------------------
columnTitle4 = "New-Golden-Path && No.hops && Time \n"  # To record the Gold service hops
csv4.write(columnTitle4)
#---------------------------------------------------------------------------------------------------
columnTitle5 = "New-Silver-Path && No.hops && Time \n"  # To record the Gold service hops
csv5.write(columnTitle5)
#---------------------------------------------------------------------------------------------------
columnTitle6 = "New-Golden-Path && No.hops && Time \n"  # To record the Gold service hops
csv6.write(columnTitle6)
#---------------------------------------------------------------------------------------------------
columnTitle7 = "New-Silver-Path && No.hops && Time \n"  # To record the Gold service hops
csv7.write(columnTitle7)
#---------------------------------------------------------------------------------------------------
csv1.close()
csv2.close()
csv3.close()
csv4.close()
csv5.close()
csv6.close()
csv7.close()

#------------------------------------------------------------------------------------------------------------------------------------
Links_weight_Dictionary = { (1, 27) : 0, (1, 2) : 0 , (1, 3) : 0 , (2, 20) : 0 , (2, 21) : 0 , (2, 23) : 0 , (3, 23) : 0 , (3, 12) : 0 , (3, 13) : 0 , (3, 17) : 0 , (4, 16) : 0 , (4, 36) : 0 , (5, 8) : 0 ,  (5, 30) : 0 , (5, 14) : 0 , (6, 33) : 0 , (6, 18) : 0 , (6, 35) : 0 , (7, 8) : 0 , (7, 9) : 0 , (7, 29) : 0 , (8, 26) : 0 , (8, 21) : 0 , (9, 24) : 0 , (9, 32) : 0 , (9, 10) : 0 , (10, 11) : 0 , (10, 36) : 0 , (10, 29) : 0 , (10, 37) : 0 , (11, 24) : 0 , (11, 35) : 0 , (12, 33) : 0 , (12, 34) : 0 , (12, 18) : 0 , (12, 35) : 0 , (13, 19) : 0 , (13, 35) : 0 , (14, 21) : 0 , (15, 25) : 0 , (15, 26) : 0 , (15, 29) : 0 , (16, 37) : 0 , (16, 22) : 0 , (17, 24) : 0 , (17, 27) : 0 , (19, 24) : 0 , (20, 28) : 0 , (20, 31) : 0 , (21, 32) : 0 , (22, 36) : 0 , (23, 28) : 0 , (25, 37) : 0 , (26, 30) : 0 , (27, 32) : 0 , (28, 34) : 0 , (31, 34) : 0}
#------------------------------------------------------------------------------------------------------------------------------------

def minimum_distance(distance, Q):
  #print "distance=", distance
  #print "Q=", Q
  min = float('Inf')
  node = 0
  for v in Q:
    if distance[v] < min:
      min = distance[v]
      node = v
  #print "min=", min, " node=", node
  return node

#-----------------------------------------------
'''
def _get_raw_path (src,dst):
  #Dijkstra algorithm
  print "src=",src," dst=", dst
  #print "myswitches=", myswitches
  distance = {}
  previous = {} 	
  sws = myswitches
 
  for dpid in sws:
    distance[dpid] = float('Inf')
    previous[dpid] = None
 
  distance[src]=0
  Q=set(sws)

  while len(Q)>0:
    u = minimum_distance(distance, Q)
    #print "u=", u
    Q.remove(u)
   
    for p in sws:
      if adjacency[u][p]!=None:
        w = 1
        if distance[u] + w < distance[p]:
          distance[p] = distance[u] + w
          previous[p] = u
  r=[]
  p=dst 
  r.append(p)
  q=previous[p]
  while q is not None:
    if q == src:
      r.append(q)
      break
    p=q
    r.append(p)
    q=previous[p] 
 
  r.reverse() 
  print " The path found by get row path is", r 
  return r 
'''
#------------------------------------------------------

def _get_raw_path_gold_path1 (src,dst):
  global G
  global P1_G
  csv2 = open(Gold_Hops_P1, "a") 
  #Dijkstra algorithm using NetworkX
  print "src=",src," dst=", dst
  p = []   # To store the shortest path

  #if src == 1 or src == 2:                   # For gold services
  p = nx.shortest_path(G, source=src, target=dst, weight='weight') 

  print " The path found by gold path function: ", p
  
  LL = []
  LL.append(src)
  LL.append(dst)
  ZZ = tuple(LL)

  row2 =  str(p) + " && " + str(len(p)-1) + " && " +  str(datetime.datetime.now()) + "\n"

  if (P1_G != len(p)-1):
     P1_G = len(p)-1
     csv2.write(row2)

  csv2.close()
  return p

#------------------------------------------------------

def _get_raw_path_gold_path2 (src,dst):
  global G
  global P2_G
  csv4 = open(Gold_Hops_P2, "a") 
  #Dijkstra algorithm using NetworkX
  print "src=",src," dst=", dst
  p = []   # To store the shortest path

  #if src == 1 or src == 2:                   # For gold services
  p = nx.shortest_path(G, source=src, target=dst, weight='weight') 

  print " The path found by gold path function: ", p
  
  LL = []
  LL.append(src)
  LL.append(dst)
  ZZ = tuple(LL)

  row4 =  str(p) + " && " + str(len(p)-1) + " && " +  str(datetime.datetime.now()) + "\n"

  if (P2_G != len(p)-1):
     P2_G = len(p)-1
     csv4.write(row4)

  csv4.close()
  return p

#------------------------------------------------------

def _get_raw_path_gold_path3 (src,dst):
  global G
  global P3_G
  csv6 = open(Gold_Hops_P3, "a") 
  #Dijkstra algorithm using NetworkX
  print "src=",src," dst=", dst
  p = []   # To store the shortest path

  #if src == 1 or src == 2:                   # For gold services
  p = nx.shortest_path(G, source=src, target=dst, weight='weight') 

  print " The path found by gold path function: ", p
  
  LL = []
  LL.append(src)
  LL.append(dst)
  ZZ = tuple(LL)

  row6 =  str(p) + " && " + str(len(p)-1) + " && " +  str(datetime.datetime.now()) + "\n"

  if (P3_G != len(p)-1):
     P3_G = len(p)-1
     csv6.write(row6)

  csv6.close()
  return p
#------------------------------------------------------
def _get_raw_path_silver_path1 (src,dst):
  global G
  global P1_S
  csv3 = open(Silver_Hops_P1, "a")
  #Dijkstra algorithm using NetworkX
  print "src=",src," dst=", dst
  p = []   # To store the shortest path

  #if src == 1 or src == 2:                   # For gold services
  #p = nx.shortest_path(G, src, dst) 
  #print " The path found by get row path is", p

  #if src == 1 or dst == 14:                   # For Bronz services
     #p = [1, 5, 7, 10, 12, 14] 
  #if src == 14 and dst==1:
     #p = [14,12,10,7,5,1]
  p = nx.shortest_path(G, src, dst) 
  print " The path found by silver path function: ", p 

  LL2 = []
  LL2.append(src)
  LL2.append(dst)
  ZZ2 = tuple(LL2)

  row3 =  str(p) + " && " + str(len(p)-1) + " && " + str(datetime.datetime.now()) +"\n"

  if (P1_S != len(p)-1):
     P1_S = len(p)-1
     csv3.write(row3)

  csv3.close()
  return p

#------------------------------------------------------
def _get_raw_path_silver_path2 (src,dst):
  global G
  global P2_S
  csv5 = open(Silver_Hops_P2, "a")
  #Dijkstra algorithm using NetworkX
  print "src=",src," dst=", dst
  p = []   # To store the shortest path

  #if src == 1 or src == 2:                   # For gold services
  #p = nx.shortest_path(G, src, dst) 
  #print " The path found by get row path is", p

  #if src == 1 or dst == 14:                   # For Bronz services
     #p = [1, 5, 7, 10, 12, 14] 
  #if src == 14 and dst==1:
     #p = [14,12,10,7,5,1]
  p = nx.shortest_path(G, src, dst) 
  print " The path found by silver path function: ", p 

  LL2 = []
  LL2.append(src)
  LL2.append(dst)
  ZZ2 = tuple(LL2)

  row5 =  str(p) + " && " + str(len(p)-1) + " && " + str(datetime.datetime.now()) +"\n"

  if (P2_S != len(p)-1):
     P2_S = len(p)-1
     csv5.write(row5)

  csv5.close()
  return p
#------------------------------------------------------
def _get_raw_path_silver_path3 (src,dst):
  global G
  global P3_S
  csv7 = open(Silver_Hops_P3, "a")
  #Dijkstra algorithm using NetworkX
  print "src=",src," dst=", dst
  p = []   # To store the shortest path

  #if src == 1 or src == 2:                   # For gold services
  #p = nx.shortest_path(G, src, dst) 
  #print " The path found by get row path is", p

  #if src == 1 or dst == 14:                   # For Bronz services
     #p = [1, 5, 7, 10, 12, 14] 
  #if src == 14 and dst==1:
     #p = [14,12,10,7,5,1]
  p = nx.shortest_path(G, src, dst) 
  print " The path found by silver path function: ", p 

  LL2 = []
  LL2.append(src)
  LL2.append(dst)
  ZZ2 = tuple(LL2)

  row7 =  str(p) + " && " + str(len(p)-1) + " && " + str(datetime.datetime.now()) +"\n"

  if (P3_S != len(p)-1):
     P3_S = len(p)-1
     csv7.write(row7)

  csv7.close()
  return p
#------------------------------------------------------

class Switch (EventMixin):
  global G
  def __init__ (self):
    self.connection = None
    self.ports = None
    self.dpid = None
    self._listeners = None
    self._connected_at = None
    #-------------------------------------------------------------------------
    #Path1 (Dublin--Sofia)
    mac_map[str("00:00:00:00:00:01")]=(18,1)   # host 1
    mac_map[str("00:00:00:00:00:02")]=(30,1)   # host 2
    mac_map[str("00:00:00:00:00:07")]=(18,2)   # host 7
    mac_map[str("00:00:00:00:00:08")]=(30,2)   # host 8
    #-------------------------------------------------------------------------
    #Path2(Humburge--Barcelona)
    mac_map[str("00:00:00:00:00:03")]=(11,1)   # host 3
    mac_map[str("00:00:00:00:00:04")]=(20,1)   # host 4
    mac_map[str("00:00:00:00:00:09")]=(11,2)   # host 9
    mac_map[str("00:00:00:00:00:10")]=(20,2)   # host 10
    #-------------------------------------------------------------------------
    #Path3(Rome--Paris)
    mac_map[str("00:00:00:00:00:05")]=(21,1)   # host 5
    mac_map[str("00:00:00:00:00:06")]=(3,1)    # host 6
    mac_map[str("00:00:00:00:00:11")]=(21,2)   # host 11
    mac_map[str("00:00:00:00:00:12")]=(3,2)    # host 12 
    #-------------------------------------------------------------------------

  def __repr__ (self):
    return dpid_to_str(self.dpid)

  def _install (self, in_port, out_port, match, buf = None):
    msg = of.ofp_flow_mod()
    msg.match = match
    msg.match.in_port = in_port
    msg.idle_timeout = 0
    msg.hard_timeout = 0
    msg.actions.append(of.ofp_action_output(port = out_port))
    msg.buffer_id = buf
    self.connection.send(msg)

  def _handle_PacketIn (self, event):
    global current_p
    print "_hanle_PacketIn() is called at", self.dpid
    packet = event.parsed
    print "packet.src=", str(packet.src), " packet.dst=", packet.dst
    print "mac_map[str(packet.src)][0]", mac_map[str(packet.src)][0]
    print "mac_map[str(packet.dst)][0]", mac_map[str(packet.dst)][0]
    #if ((str(packet.src) !="00:00:00:00:00:01" and str(packet.src) !="00:00:00:00:00:02")):
      #return   
    #if ((str(packet.src) !="00:00:00:00:00:03" and str(packet.src) !="00:00:00:00:00:04")):
       #return
    #print "switches=", switches
    #print "adjacency=", adjacency
    #-----------------------------------------------------------------------------------------------------------------------------
    if (str(packet.src) == "00:00:00:00:00:07" or str(packet.src) == "00:00:00:00:00:08"):      #We call silver function of path1
        path = _get_raw_path_silver_path1 (mac_map[str(packet.src)][0], mac_map[str(packet.dst)][0])
    
    if (str(packet.src) == "00:00:00:00:00:01" or str(packet.src) == "00:00:00:00:00:02"):      #We call gold function of path1
       path = _get_raw_path_gold_path1 (mac_map[str(packet.src)][0], mac_map[str(packet.dst)][0])
    #-----------------------------------------------------------------------------------------------------------------------------
    if (str(packet.src) == "00:00:00:00:00:09" or str(packet.src) == "00:00:00:00:00:10"):      #We call silver function of path2
        path = _get_raw_path_silver_path2 (mac_map[str(packet.src)][0], mac_map[str(packet.dst)][0])

    if (str(packet.src) == "00:00:00:00:00:03" or str(packet.src) == "00:00:00:00:00:04"):      #We call gold function of path2
       path = _get_raw_path_gold_path2 (mac_map[str(packet.src)][0], mac_map[str(packet.dst)][0])
    #-----------------------------------------------------------------------------------------------------------------------------
    if (str(packet.src) == "00:00:00:00:00:11" or str(packet.src) == "00:00:00:00:00:12"):      #We call silver function of path3
        path = _get_raw_path_silver_path3 (mac_map[str(packet.src)][0], mac_map[str(packet.dst)][0])

    if (str(packet.src) == "00:00:00:00:00:05" or str(packet.src) == "00:00:00:00:00:06"):      #We call gold function of path3
       path = _get_raw_path_gold_path3 (mac_map[str(packet.src)][0], mac_map[str(packet.dst)][0])
    #-----------------------------------------------------------------------------------------------------------------------------


    #if len(current_p)!=0 and current_p != path:
    #  del current_p[:] 

    current_p=copy.deepcopy(path)  
    print "path=", path, "current_p=", current_p
    if mac_map[str(packet.dst)][0]!=self.dpid:
      next=path[path.index(self.dpid)+1]
      #print "next=", next
      output_port = adjacency[self.dpid][next]
      #print "output_port=", adjacency[self.dpid][next]
      match = of.ofp_match.from_packet(packet)
      self._install(event.port, output_port, match) 
    else:
      output_port=mac_map[str(packet.dst)][1]
    msg = of.ofp_packet_out()
    msg.actions.append(of.ofp_action_output(port = output_port))
    msg.buffer_id = event.ofp.buffer_id
    msg.in_port = event.port
    self.connection.send(msg)

  def disconnect (self):
    if self.connection is not None:
      log.debug("Disconnect %s" % (self.connection,))
      self.connection.removeListeners(self._listeners)
      self.connection = None
      self._listeners = None

  def connect (self, connection):
    #print "type(conection.dpid)=", type(connection.dpid)
    if self.dpid is None:
      self.dpid = connection.dpid
    assert self.dpid == connection.dpid
    if self.ports is None:
      self.ports = connection.features.ports
    self.disconnect()
    log.debug("Connect %s" % (connection,))
    self.connection = connection
    self._listeners = self.listenTo(connection)
    self._connected_at = time.time()

  def _handle_ConnectionDown (self, event):
    self.disconnect() 

class l2_multi (EventMixin):
  global Links_weight_Dictionary
  global counter 
  global G


  def __init__ (self):
     context = zmq.Context.instance()
     self.socket = context.socket(zmq.PUB)  # Set up the ZMQ publisher "socket"
     self.socket.bind(PUB_URL)
     #self.scheduler = sched.scheduler(time.time, time.sleep)
     # Listen to dependencies
     def startup ():
      core.openflow.addListeners(self, priority=0)
      core.openflow_discovery.addListeners(self)
     core.call_when_ready(startup, ('openflow','openflow_discovery'))
     print "init completed"
    #-------------------------------------------
  def _handle_ConnectionUp (self, event):
      sw = switches.get(event.dpid)
      if sw is None:
        # New switch
        sw = Switch()
        switches[event.dpid] = sw
        sw.connect(event.connection)
        myswitches.append(event.dpid)
      else:
        sw.connect(event.connection)
    #-------------------------------------------
  def _handle_LinkEvent(self, event):
        global current_p
        csv1 = open(Failure_events, "a") 
        l = event.link 
        sw1 = l.dpid1 
        sw2 = l.dpid2 
        pt1 = l.port1 
        pt2 = l.port2 
        G.add_node( sw1 ) 
        G.add_node( sw2 ) 

        no_edges=0
        for p in myswitches:
          for q in myswitches:
             if adjacency[p][q]!=None: 
               no_edges+=1
        print "number of edges=", (no_edges*0.5)         
        print "current_p=", current_p
   
        if len(myswitches)==37 and (no_edges*0.5) ==56:
           if event.removed:
              print sw1, "----", sw2, " is removed"
           clear = of.ofp_flow_mod(command=of.OFPFC_DELETE)
           for dpid in current_p:
             if switches[dpid].connection is None: continue
             switches[dpid].connection.send(clear)

        if event.added:
            #print "link is added" 
            if adjacency[sw1][sw2] is None:
              adjacency[sw1][sw2] = l.port1
              adjacency[sw2][sw1] = l.port2 
              G.add_edge(sw1,sw2)   
 
        if event.removed: 
            #print "link is removed"
            try: 
                if sw2 in adjacency[sw1]: del adjacency[sw1][sw2]
                if sw1 in adjacency[sw2]: del adjacency[sw2][sw1]
                G.remove_edge(sw1,sw2) 
                
                #record the failed links
                KK = []
                KK.append(sw1)
                KK.append(sw2)
                ZZ3 = tuple(KK)
                row1 =  str(ZZ3) + " && " + str(datetime.datetime.now()) + "\n"
                csv1.write(row1)
            except: 
                print "remove edge error" 
        try: 
            #print nx.shortest_path(self.G,2,33) 
 
             N= nx.number_of_nodes(G) 
             print "Number of nodes in the current graph is: ", N             
	     E= nx.number_of_edges(G) 
             print "Number of Edges in the current graph is: ", E 
     
             if (N == 37) and (E == 57): 
 
                 print "Graph is ready now :-) " 
                 print "Graph nodes are: ",G.nodes() 
                 print "Graph edges are:", G.edges()
                 #------------------------------------
                 # Now we will assign the links weight to every edge in G
                 Edges = G.edges()
                 # Now we will assign the links weight to every edge in G
                 #if counter ==1:
                 for i in range (nx.number_of_edges(G)):
                         #print Links_weight_Dictionary[Edges[i]]
                         G[Edges[i][0]][Edges[i][1]]['weight'] = Links_weight_Dictionary[Edges[i]]
                        
                 #for i in range (nx.number_of_edges(G)): 
                        #print G.get_edge_data(Edges[i][0],Edges[i][1])
                        #print 
                 #   counter+=1
                 #------------------------------------

                 #nx.draw(self.G, with_labels=True) 
                 #plt.show() 
 
        except: 
            print "no such complete Graph yet..." 
        csv1.close()
    #-------------------------------------------
  def received_info (self, edge, prob):
      global G
      global Links_weight_Dictionary

      print '-----------------------------------'
      print 'The previous link weight list is'
      print '-----------------------------------'
      print Links_weight_Dictionary
      print '-----------------------------------'
      print "The failed link is  = {}".format(edge)
      print "The failed link probability is  = {}".format(prob)

      Link = ast.literal_eval(edge) # To convert the link from Unicode into Tuple object
      F_Probability = fast_real(prob)   # To convert the link failure probability into float
      
      Links_weight_Dictionary[Link] = F_Probability  # To update the link failure probability

      print '-----------------------------------'
      print 'The updated link weight list is'
      print '-----------------------------------'
      print Links_weight_Dictionary
      print '-----------------------------------'

#******************************************************************
def request_dispatcher():

    print "Starting request dispatcher..."
    context = zmq.Context.instance()
    socket = context.socket(zmq.REP)
    socket.bind(REQ_URL)
    while True:
        req_obj = socket.recv_json()
        print("Received request in dispatcher")
        if "type" not in req_obj:
            socket.send_json({"type": "Error", "what": "Unknown message, no 'type' field."})
            continue
        app = core.l2_multi
        type = req_obj["type"]
        #------------------------------------------------------------
        if type == "LinkFailure":

            Link = req_obj["link"]    # To get the failed link  
            Link_Probability = req_obj["probability"] # To get the link probability    
   
            core.callLater(app.received_info, Link, Link_Probability)
            socket.send_json({"type": "processing", "what": req_obj})
        else:
            socket.send_json({"type": "Error", "what": "Unknown message type."})
        #------------------------------------------------------------

#*********************************************************************        
def launch ():

    thread = threading.Thread(target=request_dispatcher)

    thread.daemon = True

    thread.start()

    core.registerNew(l2_multi)
