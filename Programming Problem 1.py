import statistics
numbers_list = [8, 0, 8, 0]

mean_value = statistics.mean(numbers_list)
median_value = statistics.median(numbers_list)
mode_value = statistics.mode(numbers_list)

print("List:", numbers_list)
print("Mode", mode_value)
print("Median", median_value)
print("Mean", mean_value)