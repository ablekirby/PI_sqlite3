# A Script to parse the Podcast Index dB
import sqlite3
from urllib.request import urlopen
import xmltodict

con = sqlite3.connect('podcastindex_feeds.db')
cur = con.cursor()

# test execute

q1 = "SELECT name FROM sqlite_master WHERE type='table';"
q2 = "PRAGMA table_info(podcasts);"
q3 = "SELECT * FROM podcasts WHERE id='937170';"
q4 = "SELECT url FROM podcasts WHERE id='937170';"
q5 = "SELECT url FROM podcasts LIMIT 1000;"
q5 = "SELECT url FROM podcasts LIMIT 1000 OFFSET 2100;"

rows = cur.execute(q5)

print("found " + str(rows.rowcount) + " rows")

rcnt = 0
for row in rows:
    rcnt = rcnt + 1
    #print(row[0])
    try:
        file=urlopen(row[0],data=None,timeout=12)
        data = file.read()
        file.close()

        try:
            data = xmltodict.parse(data)

            data = data["rss"]
            data = data["channel"]
            title = data["title"]
            data = data["item"]
            data = data[0] # first item
            data = data["enclosure"]

            nbyte = int(data['@length'])
            
            if nbyte > 100000 and nbyte < 12000000:
                print("Row " + str(rcnt) + ": " + title)
            
            #print(data)
        except:
            #print(data["channel"])
            print("Row " + str(rcnt) + ": " + "unable to parse...")
            pass


        
    except:
        print("Row " + str(rcnt) + ": " + "problem with host...")

        


print("... DONE!")
