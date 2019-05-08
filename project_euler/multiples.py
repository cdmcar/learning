
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# 1000 / 5 = 200
# 1000 / 3 = 333

threes = []
fives = []
three = 0
five = 0

for i in range(334):
    s = 3 * i
    threes.append(s)

for i in range(200):
    s = 5 * i
    if s % 3 == 0:
        pass
    else:
        fives.append(s)

for i in threes:
    three += i

for i in fives:
    five += i

answer = three + five

print(three)
print(five)
print(answer)
