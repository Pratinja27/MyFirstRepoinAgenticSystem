def read_numbers(file_name):
    numbers = []
    with open(file_name, "r") as file:
        print("File opened successfully")
        
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:  
                numbers.append(int(cleaned_line))
    
    print("Data loaded")
    return numbers


def compute_results(numbers):
    total_count = len(numbers)
    total_sum = sum(numbers)
    
    if total_count > 0:
        average_value = total_sum / total_count
    else:
        average_value = 0
    
    print("Computation completed")
    return total_count, total_sum, average_value


def write_log(file_name, count, total, average):
    with open(file_name, "a") as log_file:
        log_file.write("File opened successfully\n")
        log_file.write(f"Read {count} numbers\n")
        log_file.write(f"Sum: {total}\n")
        log_file.write(f"Average: {average}\n")
        log_file.write("Processing completed\n\n")


def main():
    input_file = "numbers.txt"
    output_file = "results.log"

    numbers_list = read_numbers(input_file)
    count, total, average = compute_results(numbers_list)
    write_log(output_file, count, total, average)


main()