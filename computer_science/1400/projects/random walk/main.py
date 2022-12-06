import statistics
import random
import math
import sys
# Pa goes in any direction randomly
# one step = one unit
# probability on second step
#   25% Pa will be 0 units away
#   25% Pa will be 2 units away
#   50% Pa will be $\sqrt{2}$ units away

# Mi-Ma
#  South twice as often as any other direction

# Reg
#   only goes east and west

walkers = {
    'Mi-Ma': 'Mi-Ma',
    'Reg': 'Reg',
    'All': 'All',
    'Pa': 'Pa'
}

def main():
    length = sys.argv[1].split(",")
    for i, len in enumerate(length):
        length[i] = int(len)

    trails = int(sys.argv[2])
    walker = sys.argv[3]

    try:
        walkers[walker]
    except KeyError:
        print("walker not supported please provide a proper one")
        return

    simulate(length, trails, walker)

def simulate(length, trails, walker):
    totals = []
    for walk in length:
        totals = []
        min = walk
        mean = 0
        max = 0

        for trail in range(0, trails):

            random.seed()

            directions = {
                "N": 0,
                "S": 0,
                "W": 0,
                "E": 0,
            }

            for step in range(0, walk):

                direction = random.randrange(0, 4)
                
                # Pa's
                if direction == 0 :
                    directions['N'] += 1
                if direction == 1 :
                    directions['S'] += 1
                if direction == 2 :
                    directions['W'] += 1
                if direction == 3 :
                    directions['E'] += 1

            x = directions['N'] - directions['S']
            y = directions['E'] - directions['W']

            distance = float("{:.2f}".format(math.sqrt((x ** 2) + (y ** 2))))

            totals.append(distance)
            mean += distance

            if distance > max:
                max = distance

            if distance < min:
                min = distance

        mean = mean/trails
        cv = statistics.stdev(totals)/mean

        print('Pa random walk of ' + str(walk) + ' steps')
        print('Mean = ' + "{:.2f}".format(mean))
        print('Max = ' + str(max))
        print('Min = ' + str(min))
        print('CV = ' + str(cv))



# def plot():

if __name__ == "__main__":
    main()