# version 2
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM musdb \
       WHERE jenre = 'ska'" 
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      band_name = row[0]
      country = row[2]
      # Now print fetched result
      print "%s,%s" % \
             (band_name, country )
except:
   print "Error: unable to fecth data"
