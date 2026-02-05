from pprint import pprint
sentence = "This is a comman interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency, width=1)

char_frequency_sortd = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=2)
print(char_frequency_sortd[0])
