input_list = '2024/day_2/input.txt'
safe_report_counter = 0
list_of_reports = []

def check_list(entries):
    increasing = True
    is_safe = True
    for idx in range(len(entries) - 1):
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
    if(is_safe):
        # print("Safe!")
        return True

with open(input_list, 'r') as file:
    for line in file:
        entries = list(map(int, line.split(" ")))
        # print(entries)
        found_safe = False
        for idx, entry in enumerate(entries):
            mod_entries = entries[:]
            mod_entries.pop(idx)
            # print(f"Modded Entries: {mod_entries}")
            found_safe = check_list(mod_entries)
            if(found_safe):
                safe_report_counter += 1
                break
        

    print(f"Safe Reports: {safe_report_counter}")

