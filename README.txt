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
Run python catalog.py will return the output.
Output will be displayed in bash as well as on your local host http://localhost:8000/


Requirements:

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

Implementation:
Constists of 3 files :
1) Catalogdb.py : Establishes connection with database news, executes the queries and returns the desired output in a dictionary.
2) Catalog.py: Acts as a web server, establishes connection to database through Catalogdb.py, builds HTML document for returning the output whenever Client/Browser requests.
3) Catalog7.html: Version1 Html file of Project, which is not yet connected to any database and is purely a front end made with the help of Owl-Carousel Magazine/Newspaper theme.
         

Views
Created 2 views:




CREATE VIEW error AS
    SELECT date(time), count(status)
    FROM log
    WHERE status != '200 OK'
    GROUP BY date(time)
    ORDER BY count(status);


CREATE VIEW full AS
    SELECT date(time), count(status)
    FROM log
    GROUP BY date(time)
    ORDER BY count(status);





Output in HTML:

Article Catalog

Most Popular Articles
Title:	Candidate is jerk, alleges rival ||	views:	338647 
Title:	Bears love berries, alleges bear ||	views:	253801 
Title:	Bad things gone, say good people ||	views:	170098 

Most Popular Authors of Popular Articles
Author Name:	Ursula La Multa ||	article:	507594 
Author Name:	Rudolf von Treppenwitz ||	article:	423457 
Author Name:	Anonymous Contributor ||	article:	170098 
Author Name:	Markoff Chaney ||	article:	84557 

Max error reported in percentage
?

Output in Text:
1. The most popular three articles of all time?
        Candidate is jerk, alleges rival: 338647 views
        Bears love berries, alleges bear: 253801 views
        Bad things gone, say good people: 170098 views
2. Who are the most popular article authors of all time?
        Ursula La Multa: 507594 views
        Rudolf von Treppenwitz: 423457 views
        Anonymous Contributor: 170098 views
        Markoff Chaney: 84557 views

references: 
https://github.com/mulligan121/log-analysis-udacity
http://www.landmarkmlp.com/js-plugin/owl.carousel/demos/images.html
https://www.w3schools.com/bootstrap4/default.asp
https://stackoverflow.com
