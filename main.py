import sys
from stats import *


if len(sys.argv) < 2:
    print("Usage: Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    print(book_report(sys.argv[1]))