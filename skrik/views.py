# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

import subprocess


import random
import MySQLdb 
import json
from collections import defaultdict

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

# urls.py-Related functions
####

@csrf_exempt
def getnew_userid(self):
## 99999999999999 is reserved for temporary errors, 00000000000000 for admin
  userid_dj = random.randint(1,99999999999998)
  while True:
    query = ('select count(id) from skrik.user where id="' + str(userid_dj) + '";')
    result = runquery(query)  
    if int(result[0]) == 0:
      break
    else:
      if userid_dj == 99999999999998:
        userid_dj = 00000000000002
      else:
        userid_dj += 1
      
  return HttpResponse(userid_dj)


@csrf_exempt
def check_user_data(self, *args, **kwargs):
  userid = kwargs.pop('userdata', None)

  result = "OK"
  return HttpResponse(result)

@csrf_exempt
def get_userid_data(self, *args, **kwargs):
  userid = kwargs.pop('username', None)
  query = ('select count(id) from skrik.msging where userid_to="' + userid + '";')

  result = runquery(query)
  return HttpResponse(result)

@csrf_exempt
def save_userdata(self, *args, **kwargs):
#  f = open('/home/aaf/Dev/aapp/server/django_test.txt', 'w')
#  f.write("Saved user data")
#  f.close()
  username_dj = kwargs.pop('username', None)
  useremail_dj = kwargs.pop('useremail', None)
  userid_dj = kwargs.pop('userid', None)
  regid_dj = kwargs.pop('regid', None)
  query_id = ('select count(id) from skrik.user where id="' + userid_dj + '";')
  exists_id = runquery(query_id)
  if exists_id[0] > 0:
    query = ('UPDATE skrik.user SET name="' + username_dj + '", email="' + useremail_dj + '", reg_id="' + regid_dj + '" WHERE id="' + userid_dj +'";')
  else:
    query = """INSERT INTO skrik.user (name, email, id, reg_id) VALUES ('%s','%s','%s','%s')""" % (username_dj,useremail_dj,userid_dj,regid_dj)
  
  result = runquery(query)
  return HttpResponse(result)

@csrf_exempt
def get_rest_of_users(self, *args, **kwargs):
  userid_dj = kwargs.pop('userid', None)
  query = ('select id, name from skrik.user where id <>"' + userid_dj + '";')
  result_aux = runquery_multiple(query)
  ctr_i = 0
  arr = []
  for i in result_aux:
    arr.append([])
    for j in i:
      arr[ctr_i].append(str(j))
    ctr_i += 1
  result = ''
  for i in arr:
    result = result + '###'
    for j in i:
      result = result + j + '///'
  return HttpResponse(result)


@csrf_exempt
def get_news(self, *args, **kwargs):
  userid_dj = kwargs.pop('userid', None)

  query = ('select id, name from skrik.user where id <>"' + userid_dj + '";')
  result_aux = runquery_multiple(query)
 
  dict = {}
  for result in result_aux:
    dict[result[0]] = result[1] 
#  result = list(result_aux)
  new_dict = {}
#  new_dict["message_01231231"] = "Hola tu que tal"
#  new_dict["message_01234231231"] = "que tal"
#  new_dict["message_0123123231"] = "memememeola tu que tal"
#  new_dict["message_012341231"] = "Holablablab tu que tal"
#  new_dict["message_10121231231"] = "Hola tfuuuu que tal"
#  new_dict["message_201231231"] = "Hola qweqweqwetu que tal"
#  new_dict["message_301231231"] = "Holashalalala tu que tal"
  result = json.dumps(dict)

  return HttpResponse(result)

@csrf_exempt
def add_poke(self, *args, **kwargs):
  userid_from = kwargs.pop('user_from', None)
  userid_to = kwargs.pop('user_to', None)

  regid_query = ('select reg_id from skrik.user where id ="' + userid_to + '";')
  regid_to = runquery(regid_query)

  p = subprocess.Popen("/home/pi/skrik/server/skrik/scripts/push.sh '" + ''.join(regid_to) + "' 'You have new pokes!'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  checkresult = ""
  for line in p.stdout.readlines():
    checkresult += ''.join(line),
  retval = p.wait()
  
  query = """INSERT INTO skrik.msging (userid_from, userid_to, status) VALUES ('%s','%s','%s')""" % (userid_from,userid_to,"sent") 

  result = runquery(query)
  return HttpResponse(checkresult)

@csrf_exempt
def cleanall_pokes(self, *args, **kwargs):
  userid = kwargs.pop('username', None)
  query = ('DELETE FROM skrik.msging WHERE userid_to="' + userid + '";')

  result = runquery(query)
  return HttpResponse(result)
