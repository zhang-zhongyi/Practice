strParam = 'Today, is the greatest day ever !'

import re
strParam = re.sub(r'[.,"\'-?:!;]', '', strParam)

max_repeat = 0
words = strParam.split()

for i in words:
    d = {}
    for letter in i:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

        if d[letter] > max_repeat:
            max_repeat = d[letter]
            ans = i

print(max_repeat, ans)