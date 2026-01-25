import random

dice_roll = random.randint(2, 5)
print(f"Ви кинули {dice_roll}")

import random

num = random.random()
print(num)

print("Hello my little\rsister")

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) 

print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Test'))

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab))

