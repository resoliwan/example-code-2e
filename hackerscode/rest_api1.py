#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests

MATCH_URL = "https://jsonmock.hackerrank.com/api/football_matches"


def request_match(params):
    res = requests.get(MATCH_URL, params)
    res.raise_for_status()
    return res.json()


def get_goals(team_pos, team, year):
    # team_pos: (team1|team2)
    # team: team_name
    # year: year
    goals = 0
    params = dict(year=year)
    params[team_pos] = team
    body = request_match(params)
    total_pages = body["total_pages"]

    for page in range(1, total_pages + 1):
        params["page"] = page
        body = request_match(params)
        goals += sum([int(match[f"{team_pos}goals"]) for match in body["data"]])

    return goals


def getTotalGoals(team, year):
    # team: team_name
    # year: year
    goals = 0
    goals += get_goals("team1", team, year)
    goals += get_goals("team2", team, year)

    return goals


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + "\n")

    fptr.close()
