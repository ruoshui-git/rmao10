# Team Nine2One (Julianna Yu, Cindy Zheng, Ruoshui Mao)
# SoftDev
# K07: Stl/O: Divine your Destiny
# 10/11/2020
# Ruoshui's _edit_ on 10/11

"""
Updated for K10
"""

import random
from typing import Dict


jobs: Dict[str, str] = {}

with open('occupations.csv', 'r') as f:
    f.readline()  # skip header
    for line in f:
        # not a good solution in reading csv in general, but works here
        [job, weight] = line.rstrip().rsplit(',', 1)
        jobs[job.strip('"')] = float(weight)
jobs.pop('Total')

names = list(jobs.keys())
weights = list(jobs.values())

def get_random() -> str:
    return random.choices(names, weights)[0]


if __name__ == "__main__":
    print(get_random())
