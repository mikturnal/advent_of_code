input_list = '2024/day_2/input.txt'
safe_report_counter = 0
list_of_reports = []


with open(input_list, 'r') as file:
    for line in file:
        increasing = True
        is_safe = True
        problem_dampener = True
        entries = list(map(int, line.split(" ")))
        print(entries)

        for idx in range(len(entries) - 1):
            # print(idx)
            if(abs(entries[idx]-entries[idx+1]) > 3):
                is_safe = False
                break
            if(idx == 0):
                if(entries[idx] == entries[idx+1]):
                    is_safe = False
                    break
                if(entries[idx] < entries[idx+1]):
                    increasing = True
                if(entries[idx] > entries[idx+1]):
                    increasing = False
            else:
                if(entries[idx] == entries[idx+1]):
                    is_safe = False
                    break
                if(entries[idx] < entries[idx+1]):
                    if(increasing == True):
                        continue
                    else:
                        is_safe = False
                        break
                if(entries[idx] > entries[idx+1]):
                    if(increasing == False):
                        continue
                    else:
                        is_safe = False
                        break
        print(is_safe)
        if(is_safe):
            safe_report_counter += 1
        
    print(f"Safe Reports: {safe_report_counter}")
