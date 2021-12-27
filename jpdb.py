# A Script to parse the Podcast Index dB
import sqlite3
from urllib.request import urlopen
import xmltodict
#from langdetect import detect
import re


con = sqlite3.connect('podcastindex_feeds.db')
cur = con.cursor()

# test execute

q1 = "SELECT name FROM sqlite_master WHERE type='table';"
q2 = "PRAGMA table_info(podcasts);"
q3 = "SELECT * FROM podcasts WHERE id='937170';"
q4 = "SELECT url FROM podcasts WHERE id='937170';"
q5 = "SELECT url FROM podcasts LIMIT 1000;"
q6 = "SELECT title FROM podcasts;"
q7 = "SELECT title FROM podcasts WHERE lastUpdate BETWEEN 1629869256 AND 1632634056;"
q8 = "SELECT title FROM podcasts WHERE dead = -1;"
q9 = "SELECT title FROM podcasts WHERE language = 'ja';"
q10 = "SELECT id FROM podcasts WHERE language = 'ja';"

#rows = cur.execute(q10)
#for row in rows:
#    print(row)

rows = cur.execute(q7)

print("found " + str(rows.rowcount) + " rows")

rcnt = 0
jcnt = 0
for row in rows:
    rcnt = rcnt + 1
    r = row[0]

    if len(r) > 1:
        try:
            #lng = detect(r)
            x = re.search("[一-龯]",r)
            if x:
                jcnt = jcnt + 1
                #print("ja" + " " + r)
        except:
            pass



print("Number of Rows: " + str(rcnt))
print("Number of Japanese: " + str(jcnt))
print("Rato: " + str(100 * jcnt / rcnt) + "%")
