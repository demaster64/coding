import random
numbers = []
reversed_numbers = []

for x in range(100):
    something = random.randint(1,100)
    numbers.append(something)

reverser = 99

for x in range(100):
   something = numbers[reverser]
   reversed_numbers.append(something)
   reverser=reverser-1

print(numbers)
print(reversed_numbers)