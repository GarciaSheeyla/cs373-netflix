#!/usr/bin/env python3
import sys
import json

# ------------
# netflix_read
# ------------

def netflix_read () :
   
     


    jsonFile = open(r'/u/sg26793/cs373G/netflix-tests/bryan-customer_cache.json','r')
    customersDict = json.loads(jsonFile.read()) 
    customerRating = (customersDict["6"])
    print(customerRating)     



netflix_read()
