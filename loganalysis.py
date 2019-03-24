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
        """
        Initialize connection and cursor as None
        """
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Create a connection with the `news` db

        Returns
        -------
        psycopg2 cursor object
            a cursor to perform database operations
        """

        self.connection = psycopg2.connect("dbname=news")
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        """
        Close the connection with the `news` db

        If inside the with statement occurs an exception this function
        prints an error message and don't throw up the exception

        Returns
        -------
        bool
            return True to don't throw up the exception
        """

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
    execute_query(query)
        Execute a query in the `news` db

    get_question_one()
        Returns the question one

    get_answer_one()
        Returns answer one formatted to print

    get_question_two()
        Returns the question two

    get_answer_two()
        Returns answer two formatted to print

    get_answer_three()
        Returns answer three formatted to print
    """

    # Log Analysis questions
    QUESTION_1 = "1. What are the most popular three articles of all time?"
    QUESTION_2 = "2. Who are the most popular article authors of all time?"
    QUESTION_3 = (
        "3. On which days did more than 1% of requests lead to errors?"
    )

    # Log Analysis queries
    QUERY_QUESTION_1 = ("SELECT a.title, "
                        "   count(b.id) AS VIEWS "
                        "FROM articles a "
                        "INNER JOIN log b ON a.slug = substring(b.path, 10) "
                        "GROUP BY a.title "
                        "ORDER BY VIEWS DESC limit 3;")

    QUERY_QUESTION_2 = ("SELECT a.name, "
                        "	count(b.id) AS VIEWS "
                        "FROM authors a "
                        "INNER JOIN articles b ON a.id = b.author "
                        "INNER JOIN log c ON b.slug = substring(c.path, 10) "
                        "GROUP BY a.name "
                        "ORDER BY VIEWS DESC;")

    QUERY_QUESTION_3 = "SELECT * FROM log;"

    def __init__(self):
        """
        Initialize answer_one, answer_two and answer_three as None
        """
        self.answer_one = None
        self.answer_two = None
        self.answer_three = None

    def execute_query(self, query):
        """
        Execute a query in the `news` db

        Parameters
        ----------
        query : str
            SQL query to be executed

        Returns
        -------
        list of tuple
            return of a SQL query
        """
        answer = ""
        with DBCursor() as cursor:
            cursor.execute(query)
            answer = cursor.fetchall()
        return answer

    def get_question_one(self):
        """
        Get the question one title

        Returns
        -------
        str
            the question one title
        """
        return self.QUESTION_1

    def get_answer_one(self):
        """
        Get the answer one formatted to print

        Execute the query `QUERY_QUESTION_1`, and convert the list of
        tuples to a string with line breaks, and the following structure:

        "Title of the article" - 9999 views

        Returns
        -------
        str
            the answer one formatted to print
        """

        self.answer_one = self.execute_query(self.QUERY_QUESTION_1)
        return "\n".join('"%s" - %s views' % tupl for tupl in self.answer_one)

    def get_question_two(self):
        """
        Get the question two title

        Returns
        -------
        str
            the question two title
        """
        return self.QUESTION_2

    def get_answer_two(self):
        """
        Get the answer two formatted to print

        Execute the query `QUERY_QUESTION_2`, and convert the list of
        tuples to a string with line breaks, and the following structure:

        "Author's name" - 9999 views

        Returns
        -------
        str
            the answer two formatted to print
        """

        self.answer_two = self.execute_query(self.QUERY_QUESTION_2)
        return "\n".join('"%s" - %s views' % tupl for tupl in self.answer_two)

    def get_answer_three(self):
        pass


def main():
    # Creating the instance of the Log Analysis
    log = LogAnalysis()

    # Print Header with version
    print "\n*** Log analysis reporting tool - Version 0.1 ***\n"

    print log.get_question_one() + "\n"
    print log.get_answer_one()
    print "\n"

    print log.get_question_two() + "\n"
    print log.get_answer_two()
    print "\n"

    # TODO: Print Question Three


if __name__ == '__main__':
    main()
