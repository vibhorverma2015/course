sentence = input()
word = input()
new_list = sentence.split(' ')
count = 0

for i in new_list:
    if i == word:
        count += 1

print("output", count)
