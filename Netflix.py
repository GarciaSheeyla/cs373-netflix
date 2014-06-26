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

  assert (int(cid) > 0 and int(cid) <= 2649429)
  assert (int(mid) > 0 and int(mid) <= 17770)

  avgCosRat = customersDict[str(cid)]
  avgStdNumRat = movieDict[str(mid)]

  movieAvg = avgStdNumRat[0]
  stdeviation = avgStdNumRat[1]
  numRat =  avgStdNumRat[2]

  s =  str(mid) + "-" + str(cid)
  actual  = cAnswerProbeDict[str(s)]

  prediction =  round( (((.521 * avgCosRat)  + (.521  * movieAvg) )  - .14) ,2) 
  # print(actual)
  assert (actual >= 0 and actual <= 5)
  alist.append(actual)
  
  assert (prediction >= 0.0 and prediction <= 5.0)
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
    return round(math.sqrt(v / s),4)


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
       assert (int(movieID) > 0 and int(movieID) <= 17770)
       netflix_write(w, 'm', movieID)
        
     else:
       customerID = line
       assert (int(customerID) > 0 and int(customerID) <= 2649429)
       prediction  = netflix_eval(movieID,customerID)
       assert (prediction >= 0.0 and prediction <= 5.0)
       plist.append(prediction)
       netflix_write(w, 'p', prediction)
  
  netflix_write(w, 'r', rmse_map_sum(alist, plist))
  return







# -------------
# netflix_write
# -------------

def netflix_write(w, cflag, data):
  assert (cflag == 'm' or cflag == 'p' or cflag == 'r')
  assert (float(data) > 0.0 and float(data) <= 2649429.0)
  
  if cflag == 'm' :
    w.write(str(data) + ":\n")
  elif cflag == 'p' :
    data  = round(data,1)
    w.write(str(data) + "\n")
  elif cflag == 'r' :
   
    w.write("RMSE: " + str(data) + "\n")
  return









