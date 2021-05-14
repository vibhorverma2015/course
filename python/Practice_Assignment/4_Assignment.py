print("please entre the word")
word = input()
list = word.split()

# print(reversed(word))
# if word == reversed(word):
#   print('true')

# j = 0
# for i in range(len(word) - 1, -1, -1):
#     if j >= i:
#         print('true')
#         break
#     elif word[i] == word[j]:
#         j += 1
#         continue
#     else:
#         print('false')
#         break

if word == word[::-1]:
    print('True')
else:
    print('false')
