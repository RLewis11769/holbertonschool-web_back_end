#!/usr/bin/env python3
""" File containing RedactingFormatter class and helper functions """
import re
import logging
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    # Class variables with same value across all instances
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        """
        Instantiate (create copy of) base class with format config and
            instance variable to be used in class

        Args:
            self: all attributes and methods of class
            fields: tuple of fields to be obfuscated
        """
        # Instantiate logging.Formatter with given format
        super(RedactingFormatter, self).__init__(self.FORMAT)
        # Instantiate instance variable tuple as list
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """
        Redact record.msg and return log record formatted by super().format

        Args:
            self: all attributes and methods of class
            record: tuple of info pertinent to event passed to LogRecord
        """
        # Format message with Formatter (5th value passed to LogRecord)
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Use regex to obfuscate fields passed in

    Args:
        fields: list of strings representing fields to obfuscate
        redaction: string representing obfuscation value
        message: string representing entire log line
        separator: string representing character separating fields in log line
    """
    for field in fields:
        # Regex pattern matching anything (.*) between field= and separator
        regex = f"(?<={field}=).*?(?={separator})"
        # re.sub uses pattern, replacement, full log string to be parsed
        message = re.sub(regex, redaction, message)
    return (message)
