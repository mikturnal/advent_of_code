input_list = '2024/day_2/input.txt'
safe_report_counter = 0

def check_list(entries):
    increasing = None
    is_safe = True

    for idx in range(len(entries) - 1):
        diff = entries[idx] - entries[idx+1]
        # check if diff over 3
        if(abs(diff) > 3):
            is_safe = False
            break
        
        # check if entries are equal
        if(diff == 0):
            is_safe = False
            break
        
        if increasing is None: # first iteration
            increasing = diff < 0
        elif (diff < 0 and not increasing) or (diff > 0 and increasing):
            is_safe = False
            break

    return is_safe

with open(input_list, 'r') as file:
    for line in file:
        entries = list(map(int, line.split(" ")))
        if(check_list(entries)):
            safe_report_counter += 1
        
    print(f"Safe Reports: {safe_report_counter}")
