import sys

pattern = "error"
count = 0
count_only = "--count" in sys.argv

with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        if pattern in line.lower():
            count += 1
            if not count_only:
                print(f"Line {line_number} : {line}", end="")

if count_only:
    print(f"Total occurrences of '{pattern}': {count}")