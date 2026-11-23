# Function 1: Make a list with WHILE loop
def get_numbers():
    numbers = []
    data = [10, 40, 30, 40, 50, 50, 35]
    i = 0
    while i < len(data):
        numbers.append(data[i])
        i += 1
    return numbers

# Function 2: Average with WHILE loop
def find_average(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    average = total / len(numbers)
    return average

# Function 3: Median and Mode with WHILE loop
def find_median_and_mode(numbers):
    sorted_list = sorted(numbers)
    n = len(sorted_list)
    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

    mode = sorted_list[0]
    max_count = 0
    i = 0
    while i < n:
        count = 0
        j = 0
        while j < n:
            if sorted_list[j] == sorted_list[i]:
                count += 1
            j += 1
        if count > max_count:
            max_count = count
            mode = sorted_list[i]
        i += 1
    return median, mode

my_list = get_numbers()
avg = find_average(my_list)
med, mod = find_median_and_mode(my_list)

print("My list:", my_list)
print("Average:", avg)
print("Median:", med)
print("Mode:", mod)




