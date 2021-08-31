import random

def PartASimulation(trials):
    # trials is the number of separate trials we will do
    # Each trial must meet this criteria: At least one of the two children is a girl.
    i = 0
    GG = 0
    while (i < trials):
        p = random.randint(1,2)
        q = random.randint(1,2)

        if((p == 2) and (q == 2)):
            # This represents the situation where neither child is a girl. Since it doesn't fit our criteria we discard it.
            continue
        elif((p == 1) and (q == 1)):
            # This represents the situation where both children are girls.
            GG += 1
        i += 1
        percent = (GG / i) * 100

        if(i % 5000 == 0):
            print("PART A: Two girls: " + str(GG) + " out of " + str(i) + " trials. " + str(round(percent,2)) + "%")

    return percent

def PartBSimulation(trials):
    # trials is the number of separate trials we will do
    # Each trial must meet this criteria: At least one of the two children is a girl named Jane.
    i = 0
    GG = 0
    while (i < trials):
        pJ = 0
        qJ = 0
        p = random.randint(1,2)
        q = random.randint(1,2)

        if(p == 1):
            # If the older child is a girl, determine if she's named Jane (1 in 50).
            pJ = random.randint(1,50)

        if((q == 1) and (pJ != 1)):
            # If the younger child is a girl who doesn't have an older sister named Jane, determine if she's named Jane (1 in 50).
            qJ = random.randint(1,50)

        if((pJ != 1) and (qJ != 1)):
            # This represents the situation where neither child is a girl named Jane. Since it doesn't fit our criteria we discard it.
            continue
        elif((p == 1) and (q == 1)):
            # This represents the situation where both children are girls.
            GG += 1
        i += 1
        percent = (GG / i) * 100

        if(i % 5000 == 0):
            print("PART B: Two girls: " + str(GG) + " out of " + str(i) + " trials. " + str(round(percent,2)) + "%")

    return percent

percentA = PartASimulation(50000)

percentB = PartBSimulation(50000)

print("FINAL OUTCOME:")
print("PART A: " + str(round(percentA,2)) + "%")
print("PART B: " + str(round(percentB,2)) + "%")