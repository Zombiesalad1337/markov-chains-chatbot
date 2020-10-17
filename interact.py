import random
import json

with open('states.json') as inputfile:
    states = json.load(inputfile)

user_input = input(">> ")
while user_input != "quit--":
    length_output = random.randrange(3,30)
    input_tokens = user_input.split(" ")
    valid_tokens = []
    for token in input_tokens:
        if token in states:
            valid_tokens.append(token)
    if len(valid_tokens) == 0:
        state = random.choice(list(states))
    else:
        state = random.choice(valid_tokens)
    
    output_string = state
    words_selected = 0
    while words_selected < length_output:
        is_next_word_state = False
        while not is_next_word_state:
            if state in states:
                next_words = states[state]
                is_next_word_state = True
            else:
                if len(valid_tokens) == 0:
                    state = random.choice(list(states))
                    next_words = states[state]
                else:
                    state = random.choice(valid_tokens)
                    next_words = states[state]

        #selects one word from top 3 words
        list_keys = []
        list_frequencies = []
        for key,value in next_words.items():
            list_keys.append(key)
            list_frequencies.append(value)
        top3keys = [x for _,x in sorted(zip(list_frequencies, list_keys))][-3:]
        high_freq_key = random.choice(top3keys)

        output_string += " "
        output_string += high_freq_key
        state = high_freq_key
        words_selected += 1
    print(output_string)
    user_input = input(">> ")

