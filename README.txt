Place your catalog project in this directory.


Log Analysis
Project Overview
This is the third project for the Udacity Full Stack Web Development . 
This project is an internal reporting tool by taking log data and calculating 
statistics from it.

Technologies Used
Backend:  Python 3 - For Integrating with Database and fetching results
Vagrant - For a dev VM for a local prod-like env
VirtualBox - Required for Vagrant
Git - Source code management
Database: PostgreSQL
FrontEnd: Bootstrap4, Html5, Css3 

Setup
Install VirtualBox and Vagrant
Clone the populated Database
Make sure vagrant is running by using the vagrant up command
Then log into vagrant using vagrant ssh
Load the data from the database using the command psql -d news -f newsdata.sql
Create views for the database as required for easier extraction
Run python catalog.py
Output will be displayed in bash as well as on your local host http://localhost:8000/

This database includes three tables:

Articles (author, title, slug, lead, body, time, id)
Authors (name, bio, id)
Log (path, ip, method, status, time, ip)

This project will be reporting following answers:
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors


Views
Views were used only for question 3 to break the problem down to understand it easier.


error view

CREATE VIEW error_view AS
    SELECT date(time), count(status)
    FROM log
    WHERE status != '200 OK'
    GROUP BY date(time)
    ORDER BY count(status);
all view

CREATE VIEW all_view AS
    SELECT date(time), count(status)
    FROM log
    GROUP BY date(time)
    ORDER BY count(status);
query_3

CREATE VIEW query_3 AS
    SELECT errors.date, e.count AS errors, errors.count AS all
    FROM all_view errors
    LEFT JOIN error_view e
    ON errors.date=e.date;
percent_error

CREATE VIEW percent_error AS
    SELECT errors.date, CAST (errors.errors as float) / errors.all * 100 AS percent
    FROM query_3 errors
    WHERE CAST (errors.errors as FLOAT) / errors.all * 100 > 1;

