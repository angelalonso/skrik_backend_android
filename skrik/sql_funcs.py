
import MySQLdb 
import sys

# GENERIC DB-Related functions 
####

def runquery(query):
  conn = MySQLdb.connect (host = "localhost",
  user = "skrik",
  passwd = "skrik123",
  db = "skrik")
  cursor = conn.cursor()

  try:
    cursor.execute(query)
    if cursor.rowcount == 0:
      result = ""
    else:
      result = cursor.fetchone()
    conn.commit()
  except:
    conn.rollback()
    return sys.exc_info()

  conn.close()
  return result


def runquery_multiple(query):
  conn = MySQLdb.connect (host = "localhost",
  user = "skrik",
  passwd = "skrik123",
  db = "skrik")
  cursor = conn.cursor()

  try:
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
  except:
    conn.rollback()
    return sys.exc_info()

  conn.close()
  return result
