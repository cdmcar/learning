# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

'''list = []
count=0

def check(var):
    count=0
    for n in range(1,21):
        count += 1
        if var % n == 0 and count < 20:
            continue
        elif count == 20:
            print(count)
            list.append(var)
            return True
        else:
            count=0

for i in range(1,10000000,1):
    if check(i) == True:
        continue
    elif check(i) == False:
        continue

print(list)'''

list = []
count = 0

for i in range(0,300000000,20):
    print(i)
    count=0
    for n in range(1,21):
        count += 1
        if count<20 and i % n == 0:
            continue
        elif count==20:
            list.append(i)
        elif i % n != 0:
            break
print(list)
