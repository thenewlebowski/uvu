
def do_research(month, adults, babies):
    result = {}

    result['adults'] = adults + babies

    result['month'] = month + 1

    result['babies'] = adults
    
    return result


def main():
    rabbits = {
        'adults': 1,
        'babies': 0,
        'month': 1,
    }
    cages = 500
    
    file = open("./rabbits.csv", "w")

    print(rabbits['month'], rabbits['adults'], rabbits['babies'], rabbits['adults'] + rabbits['babies'])

    file.write(str(rabbits['month']) + "," + str(rabbits['adults']) + "," + str(rabbits['babies']) + "," + str(rabbits['adults'] + rabbits['babies']) + "\n")



    while (rabbits['adults'] + rabbits['babies']) <= cages:

        rabbits = do_research(rabbits['month'], rabbits['adults'], rabbits['babies'])
        
        print(rabbits['month'], rabbits['adults'], rabbits['babies'], rabbits['adults'] + rabbits['babies'])

        file.write(str(rabbits['month']) + "," + str(rabbits['adults']) + "," + str(rabbits['babies']) + "," + str(rabbits['adults'] + rabbits['babies']) + "\n")
        


    print("cages will run out in month " + str(rabbits['month']))
if __name__ == "__main__":
    main()
