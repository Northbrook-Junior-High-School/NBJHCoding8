num = int(input("Enter a number: "))
# possibles = list(range(1, num + 1))
# factors = []
# for item in possibles:
#     if num % item == 0:
#         factors.append(item)
# print(factors)

print([item for item in list(range(1, num + 1)) if num % item == 0])
