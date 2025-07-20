import re

# Common SQLi patterns (can be extended)
SQLI_PATTERNS = [
    r"(?i)' *or *'1' *= *'1",      # ' OR '1'='1
    r"(?i)or *1 *= *1",            # OR 1=1
    r"(?i)union(.*?)select",       # UNION SELECT
    r"(?i)insert(.*?)into",        # INSERT INTO
    r"(?i)select(.*?)from",        # SELECT FROM
    r"(?i)drop(.*?)table",         # DROP TABLE
    r"(?i)--",                     # SQL comment
    r"(?i)#",                      # MySQL comment
    r"(?i)/\*",                    # Block comment
    r"(?i)admin' *--",             # admin' --
]

def detect_sqli(input_text):
    """
    Returns True if input matches any SQLi pattern.
    """
    for pattern in SQLI_PATTERNS:
        if re.search(pattern, input_text):
            return True
    return False
