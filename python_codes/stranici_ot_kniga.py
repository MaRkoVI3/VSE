k = int(input("Въведете общия брой цифри: "))

digits = 1
count = 9
pages = 0

while k > count * digits:
    k -= count * digits
    pages += count
    digits += 1
    count *= 10

pages += k // digits
print(pages)
