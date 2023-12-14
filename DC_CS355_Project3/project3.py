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

def airlineOne(std_dev):
    arrivals = []
    stranded = 0

    # these are arrays of all flight lengths for the respective leg of the journey.
    # using random.normal allows for the array to be generated using bell curve.
    ft_leg1 = np.random.normal(4,std_dev,10000)
    ft_leg2 = np.random.normal(4,std_dev,10000)
    ft_leg3 = np.random.normal(3.5,std_dev,10000)
    
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

    
    return stranded/10000, np.average(arrivals)


            
if __name__ == "__main__":
    devs = [.1,.2,.3,.4,.5,.6,.7,.8,.9,1,1.1,1.2]
    times = []
    strands = []
    for i in devs:
        stranded, time = airlineOne(i)
        strands.append(stranded)
        times.append(time)
    print(devs)
    print(times)
    print(strands)