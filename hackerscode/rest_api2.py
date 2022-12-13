#!/bin/python3

import math
import os
import random
import re
import sys

import requests

#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

MATCH_URL = "https://jsonmock.hackerrank.com/api/football_matches"

def request_match(params):
res = requests.get(MATCH_URL, params)
res.raise_for_status()
return res.json()


def getNumDraws(year):
goals = 0
params = dict(year=year)
for i in range(0, 10):
    params["team1goals"] = i
    params["team2goals"] = i
    body = request_match(params)
    total_pages = body["total_pages"]
    
    
    for page in range(1, total_pages + 1):
            params["page"] = page
            body = request_match(params)
            goals += sum([1 for match in body["data"]
                if match["team1goals"] == match["team2goals"]
            ]) 
        
return goals
if __name__ == '__main__':
fptr = open(os.environ['OUTPUT_PATH'], 'w')

year = int(input().strip())

result = getNumDraws(year)

fptr.write(str(result) + '\n')

fptr.close()
