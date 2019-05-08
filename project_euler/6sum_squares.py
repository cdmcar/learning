'''The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.'''

def main():

    squareofsums()
    sumofsquares()


def squareofsums():
    sums = [1,2]
    val1 = 0
    val2 = 1
    val3 = 0
    count = 2

    for i in sums:
        if count == 100:
            break
        else:
            count += 1
        val3 = sums[val1] + sums[val2]
        val1 += 1
        val2 += 1
        sums.append(val3)

    #print(sums)

def sumofsquares():
    squares = []
    list2 = []
    list3 = []
    squares[0:99] = [(k**2) for k in range(1,101)]
    val1 = 0
    val2 = 1
    val3 = 0
    count = 0

    for i in squares:
        count += 1
        val3 = i + squares[count]
        list3.append(i)
        val1 = i - 2
        val2 = i - 1
        list2.append(val3)

    print(list2)
    #print(squares)

if __name__=="__main__":
    main()
