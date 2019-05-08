# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

#str.endswith(suffix[, start[, end]])

product = []
nums = []
maxlength = 999 * 999

for i in range(1,999,1):
    for l in range(1,999,1):
        n = i * l
        if list(str(n)) == list(str(n))[::-1]:
            product.append(n)
print(max(product))
