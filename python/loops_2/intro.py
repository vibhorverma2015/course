"""
For loop version.2

for ch in "abcdefghij":
    print(ch)

ch has it values as ("a", "b","c","d"...."j")

demonsration of while loop


"""

# for ch in ("vibhor"):
#   print(ch)

#cnt = 0
# while cnt < 4:
#   print("hello!")
#  cnt += 1

# a program for search of 5 in range(1,20)

# for x in range(1, 20):
#   if(x == 5):
#      print("found")
#     break

# for x in range(0, 10):
#  if(x < 5):
#     continue
# print(x)

cnt1 = 0
while cnt1 < 5:
    cnt2 = 0
    while cnt2 < 5:
        if cnt2 == 3:
            break
        if cnt2 == 0 or cnt2 == 1:
            cnt2 += 1
            continue
        print(cnt2)
        cnt2 += 1
    cnt1 += 1
