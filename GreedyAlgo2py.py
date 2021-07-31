# -*- coding: utf-8 -*-

"""
Created on Mon Apr 19 10:58:56 2021

@author: Gobinda
"""

# -*- coding: utf-8 -*-
"""

"""
import random as r
from math import sqrt as sqrt

"""
Make n IoT nodes with random (x,y) co-ordinates
and k recharge stations
"""
n = int(input("Enter no of IoT nodes: ")) #----------------Number of IoT nodes
k = int(input("Enter no of Charging Stations: "))  #--------Number of Charging Stations 
node = []
station = []
ntn = [[1000 for i in range(n)] for j in range(n)]   #---------node to node distance nxn list
stn = [[1000 for i in range(n)] for j in range(k)]   #---------station to node distance nxk list  
computing_energy = 0.5 #------Charge in % lost per bit
travel_energy = 1 #---------Charge in % used per unit dist travelled
max_bits = 20 #-------------Assumed max computation bits in a node

class Tools:
    def __init__(s):
        s.result = 0
        
    def Edistance(s, x1, x2, y1, y2):  #Finds Distance between pt a and b 
        result = sqrt((x2-x1)**2 + (y2-y1)**2)
        return int(result)
    
    def actual_Discharge(s,a,b):   #Finds actual discharge
        c = Tools.Edistance(s, a.x, b.x, a.y, b.y)
        c = c * travel_energy
        c = c + ( b.bits * computing_energy )
        return int(c)
    
    def max_Discharge(s,a,b):   #-----Estimates max possible discharge
        c = Tools.Edistance(s, a.x, b.x, a.y, b.y)
        c = c * travel_energy
        c = c + ( max_bits * computing_energy )
        return int(c)
    
    def nearest_Node(s,a,unvisited):  #-------Find nearest node from a 
        u = unvisited
        t = []
        for i in u:
            t.append(Tools.Edistance(s, a.x, i.x, a.y, i.y)) 
        t = t.index(min(t))
        return u[t]         #-----------------return nearest unvisited node
              
    def nearest_Station(s,a):  #-------Find nearest station from a
        t = []
        for i in station:
            t.append(Tools.Edistance(s, a.x, i.x, a.y, i.y))
        t = t.index(min(t)) 
        return station[t]    #-----------------return nearest station 
    
"""
    def return_Home(s, P, C, home, stations):
        s = stations
        h = []
        path = []
        #--------Find nearest stations from home in ascending order 
        while s != []:
            t = []
            for i in s:
                t.append(Tools.Edistance(s, home.x, i.x, home.y, i.y))
            t = t.index(min(t))
            h.append(s[t])
            s.remove(s[t])
        s = stations     
        C1 = Tools.actual_Discharge(s,P,home)
        while P != home:
            if C > C1:
                P = home
                if P in station:
                    path.append(str("station-" + str(P.no) + " --> Start" ))
                elif P in node:
                    path.append(str("node-" + str(P.no) + " --> Start" ))
            else:
                for i in h:
                    C1 = Tools.actual_Discharge(s,P,home)
                    if C > C1:
                        if P in station:
                            path.append(str("station-" + str(P.no) + " --> station-" + str(i.no)))
                        elif P in node:
                            path.append(str("node-" + str(P.no) + " --> station-" + str(i.no)))
                        P = i
                        C = 100
                        break
        return path
        
"""      
    
        
class Charge_station:
    def __init__(s):
        s.x = r.randint(1,100)
        s.y = r.randint(1,100)
        s.bits = 0
        s.no = 0
    
class IoT_node:
    def __init__(s):
        s.x = r.randint(1,100)
        s.y = r.randint(1,100)
        s.bits = r.randint(5,20)
        s.no = 0

#-----------------------------initialized IoT nodes as objects
for i in range(n):
    name = str(node) + str(i)
    name = IoT_node()
    name.no = i
    node.append(name)
    
#---------------------------initialized Charging stations as objects
for i in range(k):
    name = str(station) + str(i)
    name = Charge_station()
    name.no = i
    station.append(name)
    

#---------Randomly assigned positin and computing bits of nodes

home = IoT_node()
home.x = 0
home.y = 0
home.bits = 0
home.no = "Start"

"""
node[0].x = 42
node[0].y = 43
node[0].bits = 17

node[1].x = 99
node[1].y = 67
node[1].bits = 5

node[2].x = 30
node[2].y = 17
node[2].bits = 14

node[3].x = 58
node[3].y = 13
node[3].bits = 8

node[4].x = 84
node[4].y = 29
node[4].bits = 12

node[5].x = 42
node[5].y = 35
node[5].bits = 8

node[6].x = 100
node[6].y = 97
node[6].bits = 12

node[7].x = 82
node[7].y = 70
node[7].bits = 16

node[8].x = 80
node[8].y = 10
node[8].bits = 4

node[9].x = 33
node[9].y = 79
node[9].bits = 11
"""

#---------------Randomly initialized positions for charging stations
"""
station[0].x = 17
station[0].y = 30

station[1].x = 13
station[1].y = 55

station[2].x = 70
station[2].y = 56
"""

print("\nCoordinates of IoT nodes:")
for i in range(n):
    print(str(node[i].x) + "," + str(node[i].y))

print("\nCoordinates of Charging stations:")
for i in range(k):
    print(str(station[i].x) + "," + str(station[i].y))
#---------initializing obj of Tools class

T = Tools()
   
# -------Find distance between all IoT nodes 

for i in range(n):
    for j in range(n):
        if i != j :
            x1 = node[i].x
            y1 = node[i].y
            x2 = node[j].x
            y2 = node[j].y
            ntn[i][j] = T.Edistance(x1, x2, y1, y2)
        
#-------Find distance between station and all nodes

for i in range(k):
    for j in range(n):
        x1 = station[i].x
        y1 = station[i].y
        x2 = node[j].x
        y2 = node[j].y
        stn[i][j] = T.Edistance( x1, x2, y1, y2)


"""

#--------------------show diatance between iot notes 

print("\nDistance between nodes:\n") 
for i in ntn:
    print(i)

#--------------------show the distance between nodes and station     
print("\nDistance between station and nodes:\n")

for i in stn:
    print(i)
    
"""

path = [] #------------Holds the path 
P1 = "" #--------------Nearest node from P
S = "" #--------------Nearest station from P 
S1 = "" #--------------Nearest station from P1  
P = home #-------------Current Position
C = 100 #-------------Current Charge
C1 = 0 #--------------Discharge if path is P --> S
C2 = 0 #--------------Discharge if path is P --> P1 --> S1 
U = [] #-------------Unvisited nodes
for i in node: #--------Initially all nodes are unvisited
    U.append(i)
t = []
pathx = []
pathy = []
for i in U:
    t.append( T.Edistance(P.x, i.x, P.y, i.y) ) 
t = t.index(min(t))

   
"""

Start The Designed Algorithm

"""    

while U != []:
    pathx.append(P.x)
    pathy.append(P.y)
    if P == home: 
        #print("Currenty at home")
        P1 = node[t]
        t = []
        #print("Nearest node from P is node-" + str(P1.no))
        
        for i in station:
            t.append( T.Edistance(P.x, i.x, P.y, i.y) ) 
        t = t.index(min(t))
        S = station[t]
        t = []
        #print("Nearest charging station from P is station-" + str(S.no))
        
        for i in station:
            t.append( T.Edistance(P1.x, i.x, P1.y, i.y) ) 
        t = t.index(min(t))
        S1 = station[t]
        #print("Nearest charging station from P1 is station-" + str(S1.no))
        
        C1 = T.max_Discharge(P , S) 
        C2 = T.max_Discharge(P , P1)
        C2 += T.max_Discharge(P1 , S1)
        
        if C1 <= C2:
            t =  str(P.no) + "-> station-" + str(S.no)
            path.append(t)
            P = S
            C = 100
            #print(path)
        elif C1 > C2:
            t = str(P.no) + "-> node-" + str(P1.no)
            path.append(t)
            P = P1
            C = C - T.actual_Discharge( P, P1 )
            #print(path)
            U.remove(P1)                   #---------remove the node from unvisited list
    
             
    elif P in node:
        #print("Currently at node-" + str(P.no))
        P1 = T.nearest_Node(P,U)
        #print("Nearest unvisited node from node-" + str(P.no) + " is node-" + str(P1.no))
        
        S = T.nearest_Station(P)
        #print("Nearest charging station from node-" + str(P.no) +" is station-" + str(S.no))
        
        S1 = T.nearest_Station(P1)
        #print("Nearest charging station from node-" + str(P1.no) +" is station-" + str(S1.no))
        
        C1 = T.max_Discharge(P , S) 
        C2 = T.max_Discharge(P , P1)
        C2 += T.max_Discharge(P1 , S1)
        
        if C1 <= C2:
            t =  "node-" + str(P.no) + "-> station-" + str(S.no)
            path.append(t) 
            P = S
            C = 100
            #print(path)
        elif C1 > C2:
            t = "node-" + str(P.no) + "-> node-" + str(P1.no)
            path.append(t)
            P = P1
            C = C - T.actual_Discharge( P, P1 )
            #print(path)
            U.remove(P1)                   #---------remove the node from unvisited list
            
            
            
    elif P in station:
        #print("Currently at Station-" + str(P.no))
        P1 = T.nearest_Node(P,U)
        #print("Nearest unvisited node from Station-" + str(P.no) + " is node-" + str(P1.no))
        
        t = "station-" + str(P.no) + "-> node-" + str(P1.no)
        path.append(t)
        P = P1
        C = C - T.actual_Discharge( P, P1 )
        #print(path)
        U.remove(P1)                  #---------remove the node from unvisited list 
            
print("\n")        
for i in pathx:
    print(i,end=",")
print("\n")        
for i in pathy:
    print(i,end=",")