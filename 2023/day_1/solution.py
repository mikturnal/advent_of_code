def analyse_document(input_strings):
    combined_digits_list = []

    with open(input_strings, 'r') as file:
        for line in file:
            found_written_numbers = []
            # Extracting digits from the line
            digits = [int(digit) for digit in line.strip() if digit.isdigit()]

            # Combining the first and last digits
            if digits:
                combined_digits = int(str(digits[0]) + str(digits[-1]))
                combined_digits_list.append(combined_digits)
    return sum(combined_digits_list)

input_strings = '2023/day_1/input.txt'
result = analyse_document(input_strings)
print(result)
