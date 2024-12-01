input_list = 'input.txt'
total_distance = 0
list1 = []
list2 = []

with open(input_list, 'r') as file:
    for line in file:
        two_entries = list(map(int, line.split("   ")))
        list1.append(two_entries[0])
        list2.append(two_entries[1])
        
    list1 = sorted(list1)
    list2 = sorted(list2)

    for idx, entry in enumerate(list1):
        total_distance += abs(list1[idx]-list2[idx])
        
    print(total_distance)
