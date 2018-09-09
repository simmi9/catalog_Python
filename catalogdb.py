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
# Get query results from databse and return them
def get_results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(q3_v1)
    c.execute(q3_v2)
    c.execute(q3_v3)
    c.execute(q3_v4)
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

# Print results method
def print_query_results(query_results):
    print (query_results['title'])
    for result in query_results['results']:
        print ('\t' + str(result[0]) + ': ' +
               str(result[1]) +
               query_results['ending'])

# Store query results
q1_results['results'] = get_results(q1)
q2_results['results'] = get_results(q2)
#execute query3 views

q3_results['results'] = get_results(q3)
# Print query results

print_query_results(q1_results)
print_query_results(q2_results)
#defining get posts 
def get_posts1():
    return q1_results['results']
    #return q1_results.items()
def get_posts2():
    return q2_results['results']

def get_posts3():
    return q3_results['results']






