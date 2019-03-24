#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
""" Log analysis reporting tool

TODO: Write the comments about this module, it's classes and methods.
"""

import psycopg2


class DBCursor:
    """ TODO: create a class that connects to the news db and creates a
    cursor

    The class will have __enter__ and __exit methods to be used with the
    command "with"

    """
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass


class LogAnalysis:
    """ TODO: create a class that brings the answer for the 3 questions

    The class will have __enter__ and __exit methods to be used with the
    command "with"

    """

    QUESTION_1 = "1. What are the most popular three articles of all time?"
    QUESTION_2 = "2. Who are the most popular article authors of all time?"
    QUESTION_3 = (
        "3. On which days did more than 1% of requests lead to errors?"
    )

    def __init__(self):
        pass

    def get_answer_one(self):
        pass

    def get_answer_two(self):
        pass

    def get_answer_three(self):
        pass


def main():
    # Creating the instance of the Log Analysis
    log = LogAnalysis()

    # Print Header with version
    print "\n*** Log analysis reporting tool - Version 0.1 ***\n"

    # TODO: Print Question One

    # TODO: Print Question Two

    # TODO: Print Question Three


if __name__ == '__main__':
    main()
