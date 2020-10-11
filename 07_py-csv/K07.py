# Team Nine2One (Julianna Yu, Cindy Zheng, Ruoshui Mao)
# SoftDev
# K07: Stl/O: Divine your Destiny
# 10/11/2020
# Ruoshui's _copy_ on 10/11

"""
- Read & store CSV contents in a string- Store total value in a variable
- Remove first, last, and total lines- Use a nested loop to split each occupation from its percentage
- Store job name as a key in the dictionary and percentage as a value
- Create lists to store all the job names and percentages
- Use random.choices to select a random occupation based off of the weights
- voila
"""

from random import choices

def function():
    f = open('occupations.csv', 'r')
    s = f.read()
    x = s.split('\n')
    total = float(((x[len(x) - 2]).split(","))[1])
    print(total)
    x = x[1 : len(x) - 2]
    d = {}
    keys = []
    values = []
    for i in range(len(x)):
        n = x[i]
        count = 0
        for letter in n:
            if (letter.isdigit() == False):
                count += 1
            else:
                break
        oc = n [:count - 1]
        percent = n [count:]
        keys.append(oc)
        values.append(float(percent))
        d[oc] = float(percent)
    
    return(choices(keys, weights = values, k = 1)[0])

if __name__ == "__main__":

    print(function())
