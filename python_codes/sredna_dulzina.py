n = int(input("Въведете брой стрингове: "))
strings = []

for i in range(n):
    strings.append(input(f"Въведете стринг {i+1}: "))

print(sum(len(s) for s in strings) / n)
