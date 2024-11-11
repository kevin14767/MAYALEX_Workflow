input_file = "./ErikBookCrossReference/extracted_text.txt"
with open(input_file) as file:
    lines = file.readlines()
    cholti_counter = 0
    for line in lines:
        line = line.strip()
        if line.startswith('-') and line.endswith('-'):
            continue
        elif '---------------------' in line:
            continue
        elif line.isdigit():
            continue
        else:
            cholti_counter += 1
            
    print(cholti_counter)