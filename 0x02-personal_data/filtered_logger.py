#!/usr/bin/env python3
""" File containing RedactingFormatter class and helper functions """
import logging
import mysql.connector
import re
from os import environ
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    # Class variables with same value across all instances
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
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


def get_logger() -> logging.Logger:
    """ Returns created log object and sets settings """
    # Create logger with given name
    user_data_log = logging.getLogger("user_data")
    # Set minimum level of logger to INFO
    user_data_log.setLevel(logging.INFO)
    # Make sure doesn't propagate messages to other loggers
    user_data_log.propagate = False
    # Create file handler with formatter
    handler = logging.StreamHandler()
    # Create formatter to pass fields to be obfuscated
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    # Add handler to logger
    user_data_log.addHandler(handler)
    return (user_data_log)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns database connection """
    host = environ['PERSONAL_DATA_DB_HOST']
    user = environ['PERSONAL_DATA_DB_USERNAME']
    password = environ['PERSONAL_DATA_DB_PASSWORD']
    database = environ['PERSONAL_DATA_DB_NAME']

    return (mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    ))


def main():
    """ Obtain database connection, retrieve all rows in users table,
     and display in specified format """
    log = get_logger()
    db = get_db()
    # Create cursor to execute queries with names of fields included
    cursor = db.cursor(dictionary=True)
    # Query for all rows in users table
    cursor.execute("SELECT * FROM users")
    for row in cursor:
        # Create list of tuples consisting of dict's key/value pairs
        tuple_list = row.items()
        # Convert to string of key/value pairs with separator
        str = '; '.join(f"{tuple[0]}={tuple[1]}" for tuple in tuple_list)
        # Pass string to logger to log in specified format
        log.info(str)
    db.close()


if __name__ == "__main__":
    main()
