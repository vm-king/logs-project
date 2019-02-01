#!/usr/bin/python3

#  Database reporting tool for the news database

import psycopg2

# Connect to database
DBNAME = "news"
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# Fetch most popular articles
c.execute("select title, count(title) from articles join log on "
          "concat('/article/',articles.slug) like log.path "
          "group by articles.title order by count(title) desc limit 3;")
pop_articles = c.fetchall()

# Fetch author counts
c.execute("select name, count(name) from authors inner join articles "
          "on articles.author = authors.id inner join log "
          "on concat('/article/',articles.slug) like log.path "
          "group by authors.name order by count(name) desc;")
pop_authors = c.fetchall()

# Fetch days with >1% errors
c.execute("select datecounts.time, cast(errorcounts.count as float)/"
          "cast(datecounts.count as float)*100 from datecounts "
          "join errorcounts on datecounts.time = errorcounts.time where "
          "cast(errorcounts.count as float)/cast(datecounts.count as float)"
          " > 0.01;")
error_dates = c.fetchall()

db.close()

# Print most popular artcieles
titles_list = [x[0] for x in pop_articles]
count_list = [x[1] for x in pop_articles]
print("Three most popular articles:")
for x in range(3):
    print('"'+titles_list[x] + '", ' + str(count_list[x]) + ' views')
print('\n')

# Print most popular authors
authors_list = [x[0] for x in pop_authors]
count_authors_list = [x[1] for x in pop_authors]
print("Most popular authors:")
for x in range(4):
    print(authors_list[x] + ", " + str(count_authors_list[x]) + ' views')
print('\n')

# Print dates with errors > 1%
error_date = [x[0] for x in error_dates]
error_amt = [x[1] for x in error_dates]
print("Dates with > 1 per cent  errors:")
print(str(error_date[0]) + ", " + str(round(error_amt[0], 2)) +
      " per cent errors")
