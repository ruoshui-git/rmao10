# Team Nine2One (Julianna Yu, Cindy Zheng, Ruoshui Mao)
# SoftDev
# K06: Learnination Through Amalgamation
# Re-factor 05 code
# 10/02/2020

KREWES = {
   'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
   'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
   'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

if __name__ == "__main__":

    import random

    # Combine the krewes into one list
    krew = (KREWES.get('orpheus')) + (KREWES.get('rex'))+ (KREWES.get('endymion'))

    # Print a random element from krew
    print(random.choice(krew))
