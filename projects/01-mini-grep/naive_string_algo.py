
import sys

def find_matches(text, pattern):    
    matches = []

    if not pattern:
        return matches

    last_start = len(text) - len(pattern)

    for i in range(last_start + 1):
        match = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            matches.append(i)

    return matches


def main():
    args = sys.argv[1:]
    count_only = "--count" in args

    if count_only:
        args.remove("--count")

    if len(args) != 2:
        print("Usage: python minigrep.py [--count] PATTERN FILE")
        sys.exit(1)

    pattern, filename = args

    if not pattern:
        print("Error: search pattern cannot be empty.")
        sys.exit(1)

    count = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                # Search without distinguishing uppercase and lowercase.
                matches = find_matches(line.lower(), pattern.lower())

                if matches:
                    count += 1

                    if not count_only:
                        print(
                            f"{filename}:{line_number}:{line}",
                            end="" if line.endswith("\n") else "\n"
                        )

        if count_only:
            print(count)

    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        sys.exit(1)
    except (OSError, UnicodeDecodeError) as error:
        print(f"Error reading file: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
