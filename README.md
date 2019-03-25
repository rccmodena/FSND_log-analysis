# Project: Log Analysis

This is the third project of the Udacity's Full Stack Web Developers Nanodegree.

The project consists in supposing you've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running.

It is necessary to build an internal reporting tool that will use information from a database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The questions the reporting tool should answer are:

**1. What are the most popular three articles of all time? Which articles have been accessed the most?** Present this information as a sorted list with the most popular article at the top.

**Example:**

- "Princess Shellfish Marries Prince Handsome" — 1201 views

- "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views

- "Political Scandal Ends In Political Scandal" — 553 views

**2. Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

**Example:**

- Ursula La Multa — 2304 views

- Rudolf von Treppenwitz — 1985 views

- Markoff Chaney — 1723 views

- Anonymous Contributor — 1023 views

**3. On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

**Example:**

July 29, 2016 — 2.5% errors

The program will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## Installation

To install this project you need to follow 4 major steps:

#### 1 - Virtual Machine

First, you need to install and configure a virtual machine, where the program will run. Follow the instructions [here](https://docs.python.org/3.7/library/os.html).

#### 2 - Repository

To install this repository there are two ways:
- Download the repository ZIP file and unpack it inside the vagrant directory of the virtual machine.
- Or clone the repository

```sh
$ cd FSND-Virtual-Machine/vagrant/
$ git clone https://github.com/rccmodena/log-analysis.git
$ cd log-analysis/
```

#### 3 - Database

Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant/log-analysis/ directory, which is shared with your virtual machine.

To load the data, cd into the vagrant directory and use the command:

```sh
$ psql -d news -f newsdata.sql.
```

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

#### 3 - Views

To help get the answers for the questions, it was created two views:

- articles_views

- percent_errors

You will need to create these views running the following commands, inside the folder vagrant on the vitual machine:

```sh
$ psql news
psql (9.5.14)
Type "help" for help.

news=> create view articles_views as select a.title as title, count(b.id) as number_views, a.author as author from articles a inner join log b on a.slug = substring(b.path, 10) group by a.title, a.author;
CREATE VIEW
news=> create view percent_errors as select a.log_date as log_date, round(b.request_erro * 100.0 / a.request_total, 1) as error_per_day from (select date(time) as log_date, count(id) as request_total from log group by date(time) order by date(time)) as a
news-> inner join (select date(time) as log_date, count(path) as request_erro from log a where status like '404%' group by date(time)) as b on a.log_date = b.log_date;
CREATE VIEW
news=>
```

## Requirements

This project was implemented with **Python 2.7.12**.

The Python Libraries used were:
- [psycopg2 - 2.7.7](http://initd.org/psycopg/)

The Database:
- [Postgresql 9.5.14](https://www.postgresql.org/)

## Running the Log analysis

To run the program, you only need to type the following command, inside the folder vagrant on the vitual machine:
```sh
$ python loganalysis.py
```

To see an example of output [click here](loganalysis_output.txt).

## Code Quality

To ensure code quality, it was used the tools:
- Python: [pycodestyle](https://github.com/PyCQA/pycodestyle)
- SQL: [Poor SQL](http://poorsql.com/)

## Informations about the Database

The database for this project, [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), has the following tables:

#### articles

- **id** (serial, PRIMARY KEY)
- **author** (integer, not null, FOREIGN KEY authors.id)
- **title** (text, not null)
- **slug** (text, not null, UNIQUE)
- **lead** (text)
- **body** (text)
- **time** (timestamptz, default now())

The table articles has 8 rows.

#### authors

- **id** (serial, PRIMARY KEY, FOREIGN KEY articles.author)
- **name** (text, not null)
- **bio** (text)

The table authors has 4 rows.

#### log

- **id** (serial, PRIMARY KEY)
- **path** (text)
- **ip** (inet)
- **method** (text)
- **status** (text)
- **time** (timestamptz, default now())

The table log has 1.667.735 rows.

In order to help get the answers for the questions, it was created two views:

#### articles_views

```
CREATE VIEW articles_views
AS
SELECT a.title AS title,
    count(b.id) AS number_views,
    a.author AS author
FROM articles a
INNER JOIN log b ON a.slug = substring(b.path, 10)
GROUP BY a.title,
    a.author;
```

#### percent_errors

```
CREATE VIEW percent_errors
AS
SELECT a.log_date AS log_date,
    round(b.request_erro * 100.0 / a.request_total, 1) AS error_per_day
FROM (
    SELECT DATE (TIME) AS log_date,
        count(id) AS request_total
    FROM log
    GROUP BY DATE (TIME)
    ORDER BY DATE (TIME)
    ) AS a
INNER JOIN (
    SELECT DATE (TIME) AS log_date,
        count(path) AS request_erro
    FROM log a
    WHERE STATUS LIKE '404%'
    GROUP BY DATE (TIME)
    ) AS b ON a.log_date = b.log_date;
```

## How to Contribute

If you find any bug or have a suggestion for another resources, feel free to improve this project.

First, you have to fork this repository.

Next, clone this repository to your computer to make the changes.

Once you've pushed changes to your local repository, you can issue a pull request.

## License

The contents of this repository are covered under the [MIT License](LICENSE).
