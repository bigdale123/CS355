import random

class Trial:
    first_pick_cheaper = False
    formula_swapped = False
    swap_lower = False

def trials(n):
    trials = []
    for i in range(0,n+1):
        trial = Trial()
        envelope_one = random.randint(1,10)
        envelope_two = random.randint(1,10)
        pick = random.randint(1,2)
        if pick == 1:
            if envelope_one < envelope_two:
                trial.first_pick_cheaper = True
        else:
            if envelope_two < envelope_one:
                trial.first_pick_cheaper = True
        num_flips = 0
        # tails is 0, heads is 1
        current_side = 0
        while current_side != 1:
            current_side = random.randint(0,1)
            num_flips += 1
        num_flips += .5
        if pick == 1:
            if envelope_one < num_flips:
                trial.formula_swapped = True
            if envelope_two < envelope_one and trial.formula_swapped == True:
                trial.swap_lower = True
        else:
            if envelope_two < num_flips:
                trial.formula_swapped = True
            if envelope_one < envelope_two and trial.formula_swapped == True:
                trial.swap_lower = True
        trials.append(trial)
    times_cheaper = 0
    times_swapped = 0
    times_swapped_lower = 0
    for i in trials:
        if i.first_pick_cheaper == True:
            times_cheaper += 1
        if i.formula_swapped == True:
            times_swapped += 1
        if i.swap_lower == True:
            times_swapped_lower += 1

    trial_length = len(str(n))
    print("--------------"+trial_length*"-"+"---------")
    print("  Results for "+str(n)+" Trials  ")
    print("--------------"+trial_length*"-"+"---------")
    print(" # of times 1st choice is lower:   "+str(times_cheaper))
    print(" # of times formula swapped:       "+str(times_swapped))
    print(" # of times formula swapped lower: "+str(times_swapped_lower))
    
        
            

if __name__=="__main__":
    trials(100)
    trials(1000)
    trials(10000)
    trials(100000)
    trials(1000000)
    print()
    print()
    print("# of times 1st choice is lower tends to be roughly 1/2 the # of samples")
    print("# of times formula swapped tends to be roughly 1/4 the # of samples")
    print("# of times formula swapped lower tends to be roughly 1/50 the # of samples")