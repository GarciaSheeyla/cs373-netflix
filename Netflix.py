#!/usr/bin/env python3
import sys
import json

# ------------
# netflix_read
# ------------

def netflix_read(r):
  return r.readline().rstrip("\n")



def netflix_eval(mid, cid) :
  return 1  


  jsonFile = open(r'/u/sg26793/cs373G/netflix-tests/bryan-customer_cache.json','r')
  customersDict = json.loads(jsonFile.read()) 
  print(customersDict["6"])
         
  return



def RMSE():
  return -1



def netflix_solve(r,w):
  customerID = ""

  while True :
    line = netflix_read(r)

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
  accuracy = RMSE()

  netflix_write(w, 'r', accuracy)
  return
 


def netflix_write(w, cflag, data):
  if cflag == 'm' :
    w.write(str(data) + ":\n")
  elif cflag == 'p' :
    w.write(str(data) + "\n")
  elif cflag == 'r' :
    w.write("RMSE: " + str(data) + "\n")
  return









