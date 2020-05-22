import random
from time import sleep

kazanan_numaralar= list()
for z in range(0,3):
    numbers = list(range(1, 50))
    
    for i in range(0,6):
    
        rasgele = random.randint(0 ,len(numbers) - 1)
        kazanan_numaralar.append(numbers[rasgele])
        numbers.pop(rasgele)
        t = z*i
        print(kazanan_numaralar[:t])
        sleep(0.1)

print(kazanan_numaralar)
print("Good Locck")
print("END....")

