def replace_value(values, index, new_value):
    values[index] = new_value


def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def summarize(values):
    return min(values), max(values), sum(values)


days = int(input("Enter the number of days: "))

original = []

for i in range(days):
    hours = int(input("Enter machine use time in hours: "))
    original.append(hours)

updated = original[:]

index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new number of hours: "))

replace_value(updated, index, new_value)

target = int(input("Enter the number of hours to search for: "))

target_index = find_first(updated, target)
count = updated.count(target)

minimum, maximum, total = summarize(updated)

sorted_values = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_values}")
print(f"Shortest time: {minimum}")
print(f"Longest time: {maximum}")
print(f"Total time: {total}")
print(f"Index of first {target}: {target_index}")
print(f"Number of times {target} appears: {count}")                      