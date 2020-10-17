import json

with open('movie_lines', 'rb') as inputfile:
    lines = [l.decode('utf8', 'ignore') for l in inputfile.readlines()]

with open('sentences.txt', 'w') as outputfile:
    for line in lines:
        dialogue = line.split("+++$+++ ")[-1]
        outputfile.write(dialogue)


