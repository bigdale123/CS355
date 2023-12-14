######################################################
# NOTE: If you do not have numpy installed, you will
#   Need to install it with `pip install numpy`.
#   If pip is not installed, look up the installation
#   instructions for your operating system
######################################################
import numpy as np


def convertToTime(float):
    hour = int(float)
    minute = int(60*float-hour)
    return str(hour)+":"+str(minute)[:2]

def airlineOne():
    arrivals = []
    stranded = 0

    # these are arrays of all flight lengths for the respective leg of the journey.
    # using random.normal allows for the array to be generated using bell curve.
    ft_leg1 = np.random.normal(4,.4,10000)
    ft_leg2 = np.random.normal(4,.4,10000)
    ft_leg3 = np.random.normal(3.5,.4,10000)
    
    for i in range(0,len(ft_leg1)):
        already_stranded = False
        current_time = 8 + ft_leg1[i]
        if(current_time >= 13):
            # missed both flights
            stranded += 1
        elif((current_time > (12.5-1/60)) and (current_time < 13)):
            # missed 12:30 flight, caught 13:00 flight
            current_time = 13 + ft_leg2[i]
            if(current_time >= 18):
                # missed all flights, stranded
                if already_stranded == False:
                    stranded += 1
            elif ((current_time > (17.5-1/60)) and (current_time < 18)):
                # missed 17:30 flight, caught 18:00 flight
                current_time = 18 + ft_leg3[i]
                arrivals.append(current_time)
            else:
                # caught 17:30 flight
                current_time = 17.5 + ft_leg3[i]
                arrivals.append(current_time)
        else:
            # caught 12:30 flight
            current_time = 12.5 + ft_leg2[i]
            if(current_time >= 18):
                # missed all flights, stranded
                if already_stranded == False:
                    stranded += 1
            elif ((current_time > (17.5-1/60)) and (current_time < 18)):
                # missed 17:30 flight, caught 18:00 flight
                current_time = 18 + ft_leg3[i]
                arrivals.append(current_time)
            elif ((current_time > (17.5-1/60)) and (current_time < 18)):
                # missed 17:00 flight, caught 17:30 flight
                current_time = 17.5 + ft_leg3[i]
                arrivals.append(current_time)
            else:
                # caught 17:00 flight
                current_time = 17 + ft_leg3[i]
                arrivals.append(current_time)

    print("-------------------------")
    print(" Results for Airline One ")
    print("-------------------------")
    print("Average Arrival Time: "+convertToTime(np.average(arrivals)))
    count = 0
    for arrival in arrivals:
        if arrival >= 21:
            count += 1
    print("Probability of Arriving 30 minutes after: "+str(count/10000))
    print("Probability of being stranded along the way: "+str(stranded/10000))


def airlineTwo():
    arrivals = []
    stranded = 0

    # these are arrays of all flight lengths for the respective leg of the journey.
    # using random.normal allows for the array to be generated using bell curve.
    ft_leg1 = np.random.normal(3.5,.8,10000)
    ft_leg2 = np.random.normal(4,.8,10000)
    ft_leg3 = np.random.normal(3.5,.8,10000)
    
    for i in range(0,len(ft_leg1)):
        already_stranded = False
        current_time = 8 + ft_leg1[i]
        if(current_time >= 12.5):
            # missed both flights
            stranded += 1
        elif((current_time > (12-1/60)) and (current_time < 12.5)):
            # missed 12:00 flight, caught 12:30 flight
            current_time = 12.5 + ft_leg2[i]
            if(current_time >= 17.5):
                # missed all flights, stranded
                if already_stranded == False:
                    stranded += 1
            elif ((current_time > (17-1/60)) and (current_time < 17.5)):
                # missed 17:00 flight, caught 17:30 flight
                current_time = 17.5 + ft_leg3[i]
                arrivals.append(current_time)
            else:
                # caught 17:00 flight
                current_time = 17 + ft_leg3[i]
                arrivals.append(current_time)
        else:
            # caught 12:00 flight
            current_time = 12 + ft_leg2[i]
            if(current_time >= 17.5):
                # missed all flights, stranded
                if already_stranded == False:
                    stranded += 1
            elif ((current_time > (17-1/60)) and (current_time < 17.5)):
                # missed 17:00 flight, caught 17:30 flight
                current_time = 17.5 + ft_leg3[i]
                arrivals.append(current_time)
            elif ((current_time > (16.5-1/60)) and (current_time < 17)):
                # missed 16:30 flight, caught 17:00 flight
                current_time = 17 + ft_leg3[i]
                arrivals.append(current_time)
            else:
                # caught 16:30 flight
                current_time = 16.5 + ft_leg3[i]
                arrivals.append(current_time)

    print("-------------------------")
    print(" Results for Airline Two ")
    print("-------------------------")
    print("Average Arrival Time: "+convertToTime(np.average(arrivals)))
    count = 0
    for arrival in arrivals:
        if arrival >= 20.5:
            count += 1
    print("Probability of Arriving 30 minutes after: "+str(count/10000))
    print("Probability of being stranded along the way: "+str(stranded/10000))    
        

            

airlineOne()
print()
airlineTwo()