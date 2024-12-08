

list1 = []
list2 = []

with open("input.txt", "r") as input:
    for line in input:
        first, second = line.split()
        list1.append(int(first))
        list2.append(int(second))


list1.sort()
list2.sort()


result = 0

for i in range(len(list1)):
    amount = 0
    amount = list2.count(list1[i])
    similarity = amount*list1[i]
    result += similarity
    


print(result)















