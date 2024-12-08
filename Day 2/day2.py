list = []

with open("input.txt","r") as input:
    for line in input:
        report = line.split()
        new_report = []
        for n in report:
            new_report.append(int(n))
        report = new_report
        list.append(report)
    


safeRoutes = 0

for element in list:
    isSafe = True
    if element[0] > element[1]:
        for i in range(len(element) -1):
            if element[i] <= element[i+1]:
                isSafe = False
                break
            if element[i] - 3 > element[i+1]:
                isSafe = False
                break       
    elif element[0] < element[1]:   
        for i in range(len(element) -1):
            if element[i] >= element[i+1]:
                isSafe = False
                break
            if element[i] + 3 < element[i+1]:
                isSafe = False
                break
    elif element[0] == element[1]:
        isSafe = False
    if isSafe:
        safeRoutes += 1


print(safeRoutes)

         
            
        


