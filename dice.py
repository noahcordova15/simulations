import random

roll = random.randint(1,6)
numberolls = int(input("How many times should I roll? "))

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
i = 0
while(i < numberolls):
    roll = random.randint(1,6)
    print(roll)
    if(roll == 1):
        counter1 += 1
    if(roll == 2):
        counter2 += 1
    if(roll == 3):
        counter3 += 1
    if(roll == 4):
        counter4 += 1
    if(roll == 5):
        counter5 += 1
    if(roll == 6):
        counter6 += 1
    i += 1
    
print("Number of 1's: " + str(counter1))
print("Percentage of 1's: " + str(counter1 / numberolls * 100) + "%")
print("Number of 2's: " + str(counter2))
print("Percentage of 2's: " + str(counter2 / numberolls * 100) + "%")
print("Number of 3's: " + str(counter3))
print("Percentage of 3's: " + str(counter3 / numberolls * 100) + "%")
print("Number of 4's: " + str(counter4))
print("Percentage of 4's: " + str(counter4 / numberolls * 100) + "%")
print("Number of 5's: " + str(counter5))
print("Percentage of 5's: " + str(counter5 / numberolls * 100) + "%")
print("Number of 6's: " + str(counter6))
print("Percentage of 6's: " + str(counter6 / numberolls * 100) + "%")
print("Next")
