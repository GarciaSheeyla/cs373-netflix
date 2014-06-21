#!/usr/bin/env python3
import sys
import json

# ------------
# netflix_read
# ------------

def main () :
   
     


    jsonFile = open(r"/u/mukund/cs373-netflix-tests/', 'r')
    customersDict = json.loads(jsonFile.read()) 
    customerRating = (customersDict["6"])
    
     
main()
