from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from sql_funcs import *

import random
import json

@csrf_exempt
def save_user(self, *args, **kwargs):
  username_dj = kwargs.pop('username', None)
  useraccount_dj = kwargs.pop('useraccount', None)
  userid_dj = kwargs.pop('userid', None)
  regid_dj = kwargs.pop('regid', None)
  
  if useraccount_dj[0] == "e":
    useremail_dj = useraccount_dj[1:]
    query_email = ('select id from skrik.users where email="' + useremail_dj + '";')
    exists_email = runquery(query_email)
    if exists_email == "":
      if userid_dj == "99999999999999":
        newuserid = getnew_userid_intern(useraccount_dj)
        query = """INSERT INTO skrik.users (name, email, phone, id, reg_id, status) VALUES ('%s','%s','%s','%s','%s','%s')""" % (username_dj,useremail_dj,'',newuserid,regid_dj,'active')
        query_res = runquery(query)
        result = "NEW ID = " + str(newuserid)
      else:
        query_id = ('select count(id) from skrik.users where id="' + userid_dj + '";')
        exists_id = runquery(query_id)
        result = exists_id[0]
        if exists_id[0] > 0:
          query = ('UPDATE skrik.users SET name="' + username_dj + '", email="' + useremail_dj + '", phone="", reg_id="' + regid_dj + '" WHERE id="' + userid_dj +'";')
          query_res = runquery(query)
          result = "ID found, rest updated"
        else:
          query = """INSERT INTO skrik.users (name, email, phone, id, reg_id, status) VALUES ('%s','%s','%s','%s','%s','%s')""" % (username_dj,useremail_dj,'',userid_dj,regid_dj,'active')
          result = runquery(query)
    else:
      query = ('UPDATE skrik.users SET name="' + username_dj + '", reg_id="' + regid_dj + '" WHERE email="' + useremail_dj +'";')
      query_res = runquery(query)
      result = "Email found, NEW ID = " + str(exists_email[0])

  elif useraccount_dj[0] == "p":
    userphone_dj = useraccount_dj[1:]
    query_phone = ('select id from skrik.users where phone="' + userphone_dj + '";')
    exists_phone = runquery(query_phone)
    if exists_phone == "":
      if userid_dj == "99999999999999":
        newuserid = getnew_userid_intern(useraccount_dj)
        query = """INSERT INTO skrik.users (name, email, phone, id, reg_id, status) VALUES ('%s','%s','%s','%s','%s','%s')""" % (username_dj,'',userphone_dj,newuserid,regid_dj,'active')
        query_res = runquery(query)
        result = "NEW ID = " + str(newuserid)
      else:
        query_id = ('select count(id) from skrik.users where id="' + userid_dj + '";')
        exists_id = runquery(query_id)
        result = exists_id[0]
        if exists_id[0] > 0:
          query = ('UPDATE skrik.users SET name="' + username_dj + '", email="", phone = "' + userphone_dj + '",reg_id="' + regid_dj + '" WHERE id="' + userid_dj +'";')
          query_res = runquery(query)
          result = "ID found, rest updated"
        else:
          query = """INSERT INTO skrik.users (name, email, phone, id, reg_id, status) VALUES ('%s','%s','%s','%s','%s','%s')""" % (username_dj,'',userphone_dj,userid_dj,regid_dj,'active')
          result = runquery(query)
    else:
      query = ('UPDATE skrik.users SET name="' + username_dj + '", reg_id="' + regid_dj + '" WHERE phone="' + userphone_dj +'";')
      query_res = runquery(query)
      result = "Phone found, NEW ID = " + str(exists_phone[0])
  else:
    result = "Account type invalid"
  return HttpResponse(result)


def getnew_userid_intern(useraccount_dj):
  if useraccount_dj[0] == "e": 
    useremail_dj = useraccount_dj[0]
    query_existing = ('SELECT id FROM skrik.users WHERE email="' + str(useremail_dj) + '";')
    result = runquery(query_existing);
    if result == "":

    ## 99999999999999 is reserved for temporary errors, 00000000000000 for admin
      userid_dj = random.randint(1,99999999999998)
      while True:
        query = ('SELECT count(id) FROM skrik.users WHERE id="' + str(userid_dj) + '";')
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
  elif useraccount_dj[0] == "p":
    userphone_dj = useraccount_dj[1:]
    query_existing = ('SELECT id FROM skrik.users WHERE phone="' + str(userphone_dj) + '";')
    result = runquery(query_existing);
    if result == "":

    ## 99999999999999 is reserved for temporary errors, 00000000000000 for admin
      userid_dj = random.randint(1,99999999999998)
      while True:
        query = ('SELECT count(id) FROM skrik.users WHERE id="' + str(userid_dj) + '";')
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

  else:
    userid_dj = "ERROR"

  return userid_dj



@csrf_exempt
def search_users(self, *args, **kwargs):
  word2search_dj = kwargs.pop('word2search', None)

  query = (' select name,id,status,(length(name)-length(replace(name,"' + word2search_dj + '",""))) + (length(email)-length(replace(email,"' + word2search_dj + '",""))) + length(phone)-length(replace(phone,"' + word2search_dj + '","")) as count from skrik.users where name like "%' + word2search_dj + '%" or email like "%' + word2search_dj + '%" or phone like "%' + word2search_dj + '%" order by count desc;')

  my_query = runquery_multiple(query)
  result = json.dumps(my_query)

  return HttpResponse(result)

