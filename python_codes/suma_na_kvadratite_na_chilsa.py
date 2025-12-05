n = int(input("Въведете брой числа: "))
nums = []

for i in range(n):
    nums.append(int(input(f"Въведете число {i+1}: ")))

print(sum(x*x for x in nums))
