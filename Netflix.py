#!/usr/bin/env python3
import sys
import json
import math

# ----------------
# global variables
# ----------------
  #sqsum = summation of (actual - prediction)^2
sqsum = 0
  #countn = number of square sums computed
countn = 1

# ------------
# netflix_eval
# ------------

def netflix_eval(mid, cid) :
  global sqsum
  global countn

   

  #Cache holds the average movie ratings a particular customer gives

  customerAvgJson = open(r'/u/sg26793/cs373G/netflix-tests/bryan-customer_cache.json','r')
  customersDict = json.loads(customerAvgJson.read()) 
  #avgCosRat = customersDict[str(cid)]



  #Cache holds information about each movie. The keys are the movieIDs and the value is a 3 element list that holds
  #The average movie rating, standard deviation and the number of ratings given 

  movieInfoJson = open(r'/u/sg26793/cs373G/netflix-tests/frankc-movie_cache.json','r')
  movieDict = json.loads(movieInfoJson.read())
  avgStdNumRat = movieDict[str(mid)]
#  movieAvg = avgStdNumRat[0]
#  stdeviation = avgStdNumRat[1]
 # numRat =  avgStdNumRat[2]
  
 

  #Cache hold the actual ratings for customers in probe.txt
  cAnswerProbe = open(r'/u/sg26793/cs373G/netflix-tests/osl62-AnswerCache.json','r')
  cAnswerProbeDict = json.loads(cAnswerProbe.read())
  s =  str(mid) + "-" + str(cid)
  actual  = cAnswerProbeDict[str(s)]
#  print("actual:" + str( actual))
#  print("cosavg: " + str(avgCosRat))
  
  prediction =  round(( (3 * customersDict[str(cid)])  +( 7 *  avgStdNumRat[0])) * ( .10),2)
  
 
  sqsum += (actual - prediction) ** 2
  countn += 1
  return  prediction



# -------------
# netflix_solve
# -------------

def netflix_solve(r,w):
  global sqsum
  global countn

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

    if customerID != "" :
      prediction = netflix_eval(movieID, customerID)
      # print("customer: ", customerID)
      # print("prediction: ", prediction)
      netflix_write(w, 'p', prediction)

  # print(prediction)
  accuracy = math.sqrt(sqsum * (1 / countn))

  netflix_write(w, 'r', accuracy)
  return
 


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









