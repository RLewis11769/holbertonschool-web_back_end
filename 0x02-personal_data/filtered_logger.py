import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Regex to obfuscate fields passed in """
    for field in fields:
        regex = f"(?<={field}=).*?(?={separator})"
        message = re.sub(regex, redaction, message)
    return message
