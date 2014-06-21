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
countn = 0

# ------------
# netflix_eval
# ------------

def netflix_eval(mid, cid) :
  global sqsum
  global countn

  return 1  


  customerAvgJson = open(r'/u/sg26793/cs373G/netflix-tests/bryan-customer_cache.json','r')
  customersDict = json.loads(customerAvgJson.read()) 
  print(customersDict["6"])

  sqsum += (actual - prediction) ** 2
  countn += 1
  return



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
  accuracy = math.sqrt(sqsum / countn)

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









