#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-

""" Log analysis reporting tool

This module was created for the third project of the Udacity's Full
Stack Web Developers Nanodegree, Log Analysis.

The project consists in supposing you've been hired onto a team working
on a newspaper site. The user-facing newspaper site frontend itself, and
the database behind it, are already built and running. The database
contains newspaper articles, as well as the web server log for the site.
The log has a database row for each time a reader loaded a web page.

This script is an internal reporting tool that will use information from
the database `news`, to discover what kind of articles the site's readers
like. The output of the script is shown the three predefined questions
with the respective answers. The questions are:

    1. What are the most popular three articles of all time?
    2. Who are the most popular article authors of all time?
    3. On which days did more than 1% of requests lead to errors?

This script requires that `psycopg2` be installed within the Python 2.7
environment you are running this script in. Also it needs that the
database `news` is up and running on PostgreSQL.

This file could also be imported as a module and contains the following
classes and functions:

    * class DBCursor - create a connects to the news db and returns a
    cursor

    * class LogAnalysis - create methods that brings the answer for
    the 3 questions

    * function main - the main function of the script

    TODO: VERIFY THE NECESSITY OF CREATING A VIEW IN THE DB AND PUT HERE
"""

import psycopg2


class DBCursor:
    """
    A class used to create a connection to the news db and returns a
    cursor

    This class was created to make use of the `with` statement, creating
    the methods __enter__ and __exit__ to open and close the connection.

    Attributes
    ----------
    connection : psycopg2 connection object
        a connection to the `news` db
    cursor : psycopg2 cursor object
        open a cursor to perform database operations

    Methods
    -------
    __enter__()
        Open the connection and returns a cursor

    __exit__()
        Close the cursor and the connection
    """

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = psycopg2.connect("dbname=news")
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        # Verify if the query throws an exception
        if exception_value:
            print "Error executing query!"

        # Close the connection
        self.connection.close()

        # return True to don't throw up the exception
        return True

class LogAnalysis:
    """
    A class used to save specific questions and brings it's answers from
    the `news` db.

    This class has 6 constants, 3 for the questions, and the other 3 for
    the queries to get the answer for the 3 questions.

    Attributes
    ----------
    answer_one : list of tuples
        return of the query for the question one
    answer_two : list of tuples
        return of the query for the question two
    answer_three : list of tuples
        return of the query for the question three

    Methods
    -------
    get_answer_one()
        Execute the query for the question one and returns the answer

    get_answer_two()
        Execute the query for the question two and returns the answer

    get_answer_three()
        Execute the query for the question three and returns the answer
    """

    # Log Analysis questions
    QUESTION_1 = "1. What are the most popular three articles of all time?"
    QUESTION_2 = "2. Who are the most popular article authors of all time?"
    QUESTION_3 = (
        "3. On which days did more than 1% of requests lead to errors?"
    )

    # Log Analysis ueries
    QUERY_QUESTION_1 = "SELECT * FROM articles;"
    QUERY_QUESTION_2 = "SELECT * FROM authors;"
    QUERY_QUESTION_3 = "SELECT * FROM log;"

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

    # TEST CONNECTION
    with DBCursor() as cursor:
        cursor.execute("SELECT name "
                       "FROM authors;")
        print cursor.fetchall()


if __name__ == '__main__':
    main()
