import sys


def rabin_karp(text, pattern):
    """Return all starting indexes where pattern occurs in text."""
    matches = []

    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return matches

    base = 256
    mod = 1_000_000_007
    highest_power = pow(base, m - 1, mod)

    pattern_hash = 0
    window_hash = 0

    # Calculate the pattern hash and first window hash.
    for i in range(m):
        pattern_hash = (
            pattern_hash * base + ord(pattern[i])
        ) % mod

        window_hash = (
            window_hash * base + ord(text[i])
        ) % mod

    # Slide the window across the text.
    for start in range(n - m + 1):

        # Matching hashes are candidates, not guaranteed matches.
        if window_hash == pattern_hash:
            if text[start:start + m] == pattern:
                matches.append(start)

        # Calculate the next window's hash.
        if start < n - m:
            outgoing = ord(text[start])
            incoming = ord(text[start + m])

            window_hash = (
                (window_hash - outgoing * highest_power) * base
                + incoming
            ) % mod

    return matches


def main():
    args = sys.argv[1:]
    count_only = "--count" in args

    if count_only:
        args.remove("--count")

    if len(args) != 2:
        print(
            "Usage: python minigrep_rabin_karp.py "
            "[--count] PATTERN FILE"
        )
        sys.exit(1)

    pattern, filename = args

    if not pattern:
        print("Error: search pattern cannot be empty.")
        sys.exit(1)

    count = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                matches = rabin_karp(
                    line.lower(),
                    pattern.lower()
                )

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
