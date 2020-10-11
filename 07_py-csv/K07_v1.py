# Team Nine2One (Julianna, Cindy, Ruoshui)
# SoftDev
# K07: Stl/O: Divine your Destiny
# 10/11/2020
# Ruoshui's _edit_ on 10/11

"""
- Read CSV contents line by line
- Store job name as a key in the dictionary and percentage as a value
- Create lists to store all the job names and percentages
- Use random.choices to select a random occupation based off of the weights
- voila
"""

import random

if __name__ == "__main__":
    jobs = {}
    with open('occupations.csv', 'r') as f:
        f.readline()  # skip header
        for line in f:
            # not a good solution in reading csv in general, but works here
            [job, weight] = line.rstrip().rsplit(',', 1)
            jobs[job.strip('"')] = float(weight)
    total = jobs.pop('Total')
    print(random.choices(list(jobs.keys()), list(jobs.values()))[0])
