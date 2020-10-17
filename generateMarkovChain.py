import random
import json

with open('sentences.txt','r') as f:
    sentences = f.read().splitlines()

token_count = 0
states = {}
sentence_count = 0
for sentence in sentences:
    sentence_count += 1
    if (sentence_count % 10000 == 0):
        print(sentence_count)
    tokens = sentence.split(" ")
    for i in range(len(tokens) - 1):
        currentWord = tokens[i]
        nextWord = tokens[i + 1]

        if currentWord in states:
            nextWords = states[currentWord]
            if nextWord in nextWords:
                states[currentWord][nextWord] += 1
            else:
                states[currentWord][nextWord] = 1
        else:
            states[currentWord] = {nextWord : 1}
            token_count += 1

print(token_count)

with open('states.json', 'w') as output:
    json.dump(states, output)


