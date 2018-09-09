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
q1_results['views'] = " views"
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
q2_results['views'] = " views"
#----------------------------------------------------------

# Get query results from databse and return them
def get_results(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    results = c.fetchall()
    db.close()
    return results

# Print results method
def print_results(query_results):
    print (q['title'])
    for r in q['results']:
        print ('\t' + str(r[0]) + ': ' +
               str(r[1]) +
               q['views'])

# Store query results
q1_results['results'] = get_results(q1)
q2_results['results'] = get_results(q2)


# Print query results

print_results(q1_results)
print_results(q2_results)

#-------------------------------------------------
#defining get posts 
def get_posts1():
    return q1_results['results']
    #return q1_results.items()
  
def get_posts2():
    return q2_results['results']







