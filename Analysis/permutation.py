import csv, random

### Initialize Iteration Count
iterationCount = 0

### Define Headers for writing to output csv:
headers = ["Iteration","Breitbart","PinkNews"]

with open("BiologicalPermutation.csv","w") as outputFile:
    w = csv.writer(outputFile)
    w.writerow(headers)
    for iteration in range(10001):
        ### Initializing Counts
        BreitbartCount = 0
        PinkNewsCount = 0
        ### Initializing csv List for writing to output csv
        csvList = []
        ### Count up iterations
        iterationCount += 1
        csvList.append(iterationCount)
        for occurrence in range(672):
            choices = ["Breitbart","PinkNews"]
            selection = random.choice(choices)
            if selection == "Breitbart":
                BreitbartCount += 1
            elif selection == "PinkNews":
                PinkNewsCount += 1
        csvList.append(BreitbartCount)
        csvList.append(PinkNewsCount)
        w.writerow(csvList)





