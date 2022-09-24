primes = [2,3,5,7]
for i in primes:
    print(i)

#########################################

for i in range(5):
    print(i)

for i in range(3,6):
    print(i)

for i in range(3,8,2):
    print(i)

#########################################

y=0
while y<5:
    print(y)
    y+=1

#########################################

z=0
while True:
    print(z)
    z+=1
    if z > 5:
        break

print("if i%2 == 0:")
for i in range(10):
    if i%2 == 0:
        continue
    print(i)

#########################################

print("---------2-------")
for i in range(1,10):
    if (i%5 == 0):
        break
    print(i)
else:
    print("printed cos statement failed")

print("----------------")
for i in range(1,10):
    print(i)
print("----------------")
for i in range(10):
    print(i)
print("--------1--------")
for i in range(10):
    print(i%5)