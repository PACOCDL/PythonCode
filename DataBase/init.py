# code=utf8
import MySQLdb

cxn = MySQLdb.connect('localhost', 'root', '1234', 'jspclass')
cur=cxn.cursor()
cur.execute("SELECT VERSION()")
data=cur.fetchone()
print 'data version is %s' % data
# print "Database version : %s " % data
cxn.close()