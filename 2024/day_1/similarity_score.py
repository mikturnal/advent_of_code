input_list = '2024/day_1/input.txt'
similarity_score = 0
list1 = []
list2 = []

with open(input_list, 'r') as file:
    for line in file:
        two_entries = list(map(int, line.split("   ")))
        list1.append(two_entries[0])
        list2.append(two_entries[1])

    for idx, entry in enumerate(list1):
        counter = 0
        for idy, entry2 in enumerate(list2):
            if(list1[idx] == list2[idy]):
                counter += 1
        
        similarity_score += counter * entry
    
    print(similarity_score)
        