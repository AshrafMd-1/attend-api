import json


def dum():
    f = open('value\dummy.json', 'r')
    data = f.read()
    f.close()
    return data
