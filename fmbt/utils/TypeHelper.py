"""
Functions to call for typing text in different forms.
"""

import random

firstnames = []
lastnames = []
domains = []

adjectives = []
nouns = []
verbs = []

def initWords():
    global firstnames
    global lastnames
    global domains
    global adjectives
    global nouns
    global verbs

    with open("../utils/assets/firstnames.txt") as f:
        firstnames = f.readlines()

    with open("../utils/assets/lastnames.txt") as f:
        lastnames = f.readlines()

    with open("../utils/assets/domains.txt") as f:
        domains = f.readlines()

    with open("../utils/assets/adjectives.txt") as f:
        adjectives = f.readlines()

    with open("../utils/assets/nouns.txt") as f:
        nouns = f.readlines()

    with open("../utils/assets/verbs.txt") as f:
        verbs = f.readlines()

def getUsername():
    global firstnames
    global lastnames
    global domains

    msg = random.choice(firstnames).strip() + "." + random.choice(lastnames).strip() + "@" + random.choice(domains).strip()
    msg = msg.lower()
    return msg

def getBoardName():
    global adjectives
    global nouns

    msg = random.choice(adjectives).strip() + " " + random.choice(nouns).strip()
    msg = msg.capitalize()
    return msg

def getTicketName():
    global adjectives
    global nouns
    global verbs

    msg = random.choice(verbs).strip() + " " + random.choice(adjectives).strip() + " " + random.choice(nouns).strip()
    msg = msg.capitalize()
    return msg

def getTicketContent():
    global adjectives
    global nouns
    global verbs

    msg = "- " + random.choice(verbs).strip() + " " + random.choice(adjectives).strip() + " " + random.choice(nouns)
    return msg

def getUrl():
    global domains
    global nouns
    msg = "www." + random.choice(domains).strip() + "/" +  random.choice(nouns).strip()
    return msg

def getWord():
    return random.choice(nouns).strip()