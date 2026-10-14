
# MiniGrep

A command-line text search tool built to explore string-matching
algorithms and practical software engineering principles.

## Implementations

- **Naive string matching:** compares characters directly.
- **Rabin–Karp:** uses hashing and a rolling window to search for patterns.

## Concepts

- String processing
- Algorithmic complexity
- Command-line arguments
- Error handling
- Case-insensitive search

## Requirements

Python 3.10 or later.

## Usage

From the repository root:

```bash
python projects/01-mini-grep/minigrep.py error projects/01-mini-grep/sample.txt
```

```bash
python projects/01-mini-grep/minigrep_rabin_karp.py error projects/01-mini-grep/sample.txt
```

Count matching lines:

```bash
python projects/01-mini-grep/minigrep.py --count error projects/01-mini-grep/sample.txt
```

## Testing

Planned test coverage includes:
- Matching and non-matching patterns
- Case-insensitive search
- Overlapping matches
- Empty patterns and files
- Missing files

## Performance

The naive and Rabin–Karp implementations will be compared using
the same inputs to examine their practical performance and trade-offs.

## Future Improvements

- Automated unit tests
- Performance benchmarks
- Additional search options
