import random
from matplotlib import pyplot as plt


def trial():
    # function returns time spent waiting on next train
    time = random.randint(710, 730)
    # print(time)
    if time <= 715:
        return time, 715-time
    elif 715 < time and time <= 730:
        return time, 730-time 

if __name__=="__main__":
    arrivals = []
    waits = []
    for i in range(0, 101):
        time, wait = trial()
        arrivals.append(time)
        waits.append(wait)
    fig, axis = plt.subplots(figsize=(10,5))
    # I tried setting the bins of the graph here to 2 minute intervals, but it
    #   Doesnt work....
    axis.hist(arrivals, bins=range(710,730,2), edgecolor='black', linewidth=1)
    plt.show()
    
        