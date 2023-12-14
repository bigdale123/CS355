import random
import numpy as np

def trials(n):
    numbers1 = []
    numbers2 = []
    numbers3 = []
    for i in range(0,n+1):
        numbers1.append(random.randint(-1,1))
    for i in range(0,n+1):
        numbers2.append(random.randint(-1,1))
    for i in range(0,n+1):
        numbers3.append(random.randint(-1,1))
    print("----- Results for N = "+str(n)+" -----")
    print("Average for Trial 1: "+str(np.average(numbers1)))
    print("Std Dev for Trial 1: "+str(np.std(numbers1)))
    print("Average for Trial 2: "+str(np.average(numbers2)))
    print("Std Dev for Trial 2: "+str(np.std(numbers2)))
    print("Average for Trial 3: "+str(np.average(numbers3)))
    print("Std Dev for Trial 3: "+str(np.std(numbers3)))
    print()
    print()

trials(10)
trials(100)
trials(1000)
trials(10000)
trials(100000)
    
