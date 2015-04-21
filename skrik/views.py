# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

import subprocess

from sql_funcs import *
from user_funcs import *
from msg_funcs import *

import random
import json
from collections import defaultdict

import sys



# urls.py-Related functions
####

@csrf_exempt
def getnew_userid(self, *args, **kwargs):
  useremail_dj = kwargs.pop('useremail', None)
  query_existing = ('select id from skrik.users where email="' + str(useremail_dj) + '";')
  result = runquery(query_existing);
  if result == "":

  ## 99999999999999 is reserved for temporary errors, 00000000000000 for admin
    userid_dj = random.randint(1,99999999999998)
    while True:
      query = ('select count(id) from skrik.users where id="' + str(userid_dj) + '";')
      result = runquery(query)  
      if int(result[0]) == 0:
        break
      else:
        if userid_dj == 99999999999998:
          userid_dj = 00000000000002
        else:
          userid_dj += 1
  else:
    userid_dj = result
      
  return HttpResponse(userid_dj)


# TO BE DELETED
def getnew_userid_intern(useremail_dj):
  query_existing = ('select id from skrik.users where email="' + str(useremail_dj) + '";')
  result = runquery(query_existing);
  if result == "":

  ## 99999999999999 is reserved for temporary errors, 00000000000000 for admin
    userid_dj = random.randint(1,99999999999998)
    while True:
      query = ('select count(id) from skrik.users where id="' + str(userid_dj) + '";')
      result = runquery(query)  
      if int(result[0]) == 0:
        break
      else:
        if userid_dj == 99999999999998:
          userid_dj = 00000000000002
        else:
          userid_dj += 1
  else:
    userid_dj = result
      
  return userid_dj



@csrf_exempt
def get_userid_data(self, *args, **kwargs):
  userid = kwargs.pop('username', None)
  query = ('select count(id) from skrik.msgs where userid_to="' + userid + '";')

  result = runquery(query)
  return HttpResponse(result)



@csrf_exempt
def get_userid_username(self, *args, **kwargs):
  userid = kwargs.pop('userid', None)
  query = ('select name from skrik.users where id="' + userid + '";')

  result = runquery(query)
  return HttpResponse(result)


# TO BE DELETED
@csrf_exempt
def save_userdata(self, *args, **kwargs):
  username_dj = kwargs.pop('username', None)
  useremail_dj = kwargs.pop('useremail', None)
  userid_dj = kwargs.pop('userid', None)
  regid_dj = kwargs.pop('regid', None)
  query_email = ('select id from skrik.users where email="' + useremail_dj + '";')
  exists_email = runquery(query_email)
   
  if exists_email == "":
    if userid_dj == "99999999999999":
      newuserid = getnew_userid_intern(useremail_dj)
      query = """INSERT INTO skrik.users (name, email, id, reg_id) VALUES ('%s','%s','%s','%s')""" % (username_dj,useremail_dj,newuserid,regid_dj)
      query_res = runquery(query)
      result = "NEW ID = " + str(newuserid)
    else:
      query_id = ('select count(id) from skrik.users where id="' + userid_dj + '";')
      exists_id = runquery(query_id)
      result = exists_id[0]
      if exists_id[0] > 0:
        query = ('UPDATE skrik.users SET name="' + username_dj + '", email="' + useremail_dj + '", reg_id="' + regid_dj + '" WHERE id="' + userid_dj +'";')
        query_res = runquery(query)
        result = "ID found, rest updated"
      else:
        query = """INSERT INTO skrik.users (name, email, id, reg_id) VALUES ('%s','%s','%s','%s')""" % (username_dj,useremail_dj,userid_dj,regid_dj)
        result = runquery(query)
  else:
    query = ('UPDATE skrik.users SET name="' + username_dj + '", reg_id="' + regid_dj + '" WHERE email="' + useremail_dj +'";')
    query_res = runquery(query)
    result = "Email found, NEW ID = " + str(exists_email[0])
  return HttpResponse(result)



@csrf_exempt
def save_userdata_old(self, *args, **kwargs):
  username_dj = kwargs.pop('username', None)
  useremail_dj = kwargs.pop('useremail', None)
  userid_dj = kwargs.pop('userid', None)
  regid_dj = kwargs.pop('regid', None)
  query_id = ('select count(id) from skrik.users where id="' + userid_dj + '";')
  exists_id = runquery(query_id)
  if exists_id[0] > 0:
    query = ('UPDATE skrik.users SET name="' + username_dj + '", email="' + useremail_dj + '", reg_id="' + regid_dj + '" WHERE id="' + userid_dj +'";')
  else:
    query = """INSERT INTO skrik.users (name, email, id, reg_id) VALUES ('%s','%s','%s','%s')""" % (username_dj,useremail_dj,userid_dj,regid_dj)
  
  result = runquery(query)
  return HttpResponse(result)



@csrf_exempt
def get_rest_of_users(self, *args, **kwargs):
  userid_dj = kwargs.pop('userid', None)
  query = ('select id, name from skrik.users where id <>"' + userid_dj + '";')
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


# TO BE DELETED
@csrf_exempt
def get_news_old(self, *args, **kwargs):
  userid_dj = kwargs.pop('userid', None)

  query = ('select userid_from,message,status,timestamp,id from skrik.msgs where userid_to ="' + userid_dj + '";')

  my_query = runquery_multiple(query) 
  result = json.dumps(my_query)

  return HttpResponse(result)


# TO BE DELETED
@csrf_exempt
def add_message_old(self, *args, **kwargs):
  message = kwargs.pop('message', None)
  userfrom = kwargs.pop('userfrom', None)
  userto = kwargs.pop('userto', None)
  timestamp = kwargs.pop('timestamp', None)

  query = ('insert into skrik.msgs (userid_from,userid_to,message,status,timestamp) values ("' + userfrom + '","' + userto + '","' + message + '","sent",' + timestamp + ');')

  result = runquery(query)

  return HttpResponse(result)

  


@csrf_exempt
def add_poke(self, *args, **kwargs):
  userid_from = kwargs.pop('user_from', None)
  userid_to = kwargs.pop('user_to', None)

  regid_query = ('select reg_id from skrik.users where id ="' + userid_to + '";')
  regid_to = runquery(regid_query)

  p = subprocess.Popen("/home/pi/skrik/server/skrik/scripts/push.sh '" + ''.join(regid_to) + "' 'You have new pokes!'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  checkresult = ""
  for line in p.stdout.readlines():
    checkresult += ''.join(line),
  retval = p.wait()
  
  query = """INSERT INTO skrik.msgs (userid_from, userid_to, status) VALUES ('%s','%s','%s')""" % (userid_from,userid_to,"sent") 

  result = runquery(query)
  return HttpResponse(checkresult)



@csrf_exempt
def cleanall_pokes(self, *args, **kwargs):
  userid = kwargs.pop('username', None)
  query = ('DELETE FROM skrik.msgs WHERE userid_to="' + userid + '";')

  result = runquery(query)
  return HttpResponse(result)
