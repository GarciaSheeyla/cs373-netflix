#!/usr/bin/env python3
import sys
import json
import math
from functools import reduce
import fileinput
# ----------------
# global variables
# -------------

global alist
alist = []

global plist
plist = []

#Cache holds the average movie ratings a particular customer gives
customersDict = {}
with open(r'/u/mukund/netflix-tests/bryan-customer_cache.json', 'r') as file:
  customersDict = json.load(file)




#Cache holds information about each movie. The keys are the movieIDs and the value is a 3 element list that holds
#The average movie rating, standard deviation and the number of ratings given
movieDict  = {}
with open(r'/u/mukund/netflix-tests/frankc-movie_cache.json','r') as file:
  movieDict = json.load(file)



#Cache hold the actual ratings for customers in probe.txt
#  cAnswerProbe = open(r'/u/mukund/netflix-tests/osl62-AnswerCache.json','r')

cAnswerProbeDict = {}
with open(r'/u/mukund/netflix-tests/osl62-AnswerCache.json','r') as file:
  cAnswerProbeDict = json.load(file)

# ------------
# netflix_eval
# ------------

def netflix_eval(mid, cid) :
  global alist

  avgCosRat = customersDict[str(cid)]
  avgStdNumRat = movieDict[str(mid)]

  movieAvg = avgStdNumRat[0]
  #  stdeviation = avgStdNumRat[1]
  # numRat =  avgStdNumRat[2]

  s =  str(mid) + "-" + str(cid)
  actual  = cAnswerProbeDict[str(s)]

  prediction =  round( ((.521 * avgCosRat)  + (.521  * movieAvg) )  - .14 , 2) 

  alist.append(actual)
  
  return  prediction



def rmse_map_sum (a, p) :
    """
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    assert(len(a) == len(p))
    s = len(a)
    v = sum(map(sqre_diff, a, p))
    return math.sqrt(v / s)


def sqre_diff (x, y) :
    return (x - y) ** 2


# -------------
# netflix_solve
# -------------

def netflix_solve(r,w):
  global plist
  global alist
    
  for line in fileinput.input():
     line = line.rstrip("\n")
     if (line == ""):
         break
     if (line[-1] == ':'):
       movieID = line.rstrip(":")
       netflix_write(w, 'm', movieID)
        
     else:
       customerID = line
       prediction  = netflix_eval(movieID,customerID)
       plist.append(prediction)
       netflix_write(w, 'p', prediction)
  
  netflix_write(w, 'r', rmse_map_sum(alist, plist))
  return




"""
  customerID = ""

  while True :
    line = r.readline().rstrip("\n")

    if not line : #failed read, done
      break

    if (line[-1] == ':') :
      movieID = line.rstrip(":")
      netflix_write(w, 'm', movieID)
      customerID = ""
      # print("\nmovie: ", movieID)
    else :
      customerID = line
    plist = []
    if customerID != "" :
      prediction = netflix_eval(movieID, customerID)
      # print("customer: ", customerID)
      # print("prediction: ", prediction)
      netflix_write(w, 'p', prediction)
       
      plist.append(prediction)


  accuracy = rmse_map_sum(plist,alist)

  netflix_write(w, 'r', accuracy)
  return
 """


# -------------
# netflix_write
# -------------

def netflix_write(w, cflag, data):



  if cflag == 'm' :
    w.write(str(data) + ":\n")
  elif cflag == 'p' :
    w.write(str(data) + "\n")
  elif cflag == 'r' :
   
    w.write("RMSE: " + str(data) + "\n")
  return









