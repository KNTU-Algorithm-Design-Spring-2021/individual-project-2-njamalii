import time
import json

import redis

redis_connection = redis.Redis('localhost')

with open('words_dictionary.json') as json_file:
    words_dictionary = json.load(json_file)

redis_connection.mset(words_dictionary)

user_text = input("Pleas Enter You're String: \n")

meaning_full_words = []


def valid(string: str) -> bool:
    if redis_connection.exists(string.lower()) == 0:
        return False
    else:
        meaning_full_words.append(string)
        return True


start_time = time.time()

for i in range(0, len(user_text)):
    temp = []
    for j in range(0, len(user_text) + 2):
        temp = []
        if len(temp) == i:
            valid(''.join(temp))
        else:
            temp.append(user_text[i-1:j])
            valid(''.join(temp))

meaning_full_words = list(set(meaning_full_words))

print(meaning_full_words)

print("Execution Time --- %s seconds ---" % (time.time() - start_time))
