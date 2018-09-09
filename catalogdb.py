#!/bin/python3
import psycopg2, bleach
import datetime


# "Database code" for the DB Forum.
DBNAME = "news"

q1 = ("""SELECT title, count(*) as num FROM articles, log
      WHERE articles.slug = substring(log.path, 10)
      GROUP BY title ORDER BY num DESC LIMIT 3;""")
# Store results
q1_results = dict()
q1_results['title'] = (
    "1. The most popular three articles of all time?")
q1_results['ending'] = " views"
#-------------------------------------------------------------

q2 = ("""SELECT authors.name, count(*) AS num
      FROM articles
      JOIN authors on articles.author = authors.id
      JOIN log on articles.slug = substring(log.path, 10)
      WHERE log.status LIKE '200 OK'
      GROUP BY authors.name ORDER BY num desc;""")
q2_results = dict()
q2_results['title'] = (
    "2. Who are the most popular article authors of all time?")
q2_results['ending'] = " views"
#----------------------------------------------------------
q3 = ("""SELECT to_char(errors.date, 'Mon DD, YYYY'),
      round( cast(errors.percent as numeric), 3) FROM percent_error errors;""")

q3_results = dict()
q3_results['title'] = (
    "3. On which days did more than 1% of requests lead to errors?")
q3_results['ending'] = ""


q3_v1 = (""" CREATE VIEW error_view AS
    SELECT date(time), count(status)
    FROM log
    WHERE status != '200 OK'
    GROUP BY date(time)
    ORDER BY count(status);  """)


q3_v2 = (""" CREATE VIEW all_view AS
    SELECT date(time), count(status)
    FROM log
    GROUP BY date(time)
    ORDER BY count(status);""")

q3_v3 = ("""CREATE VIEW query_3 AS
    SELECT errors.date, e.count AS errors, errors.count AS all
    FROM all_view errors
    LEFT JOIN error_view e 
    ON errors.date=e.date; """)
q3_v4 = ("""CREATE VIEW percent_error AS
    SELECT errors.date, CAST (errors.errors as float) / errors.all * 100 AS percent
    FROM query_3 errors
    WHERE CAST (errors.errors as FLOAT) / errors.all * 100 > 1; """)





POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  POSTS.append((content, datetime.datetime.now()))


