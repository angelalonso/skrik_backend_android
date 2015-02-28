from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from sql_funcs import *

import random
import json

@csrf_exempt
def add_message(self, *args, **kwargs):
  message = kwargs.pop('message', None)
  userfrom = kwargs.pop('userfrom', None)
  userto = kwargs.pop('userto', None)
  timestamp = kwargs.pop('timestamp', None)

  query = ('insert into skrik.msgs (userid_from,userid_to,message,status,timestamp) values ("' + userfrom + '","' + userto + '","' + message + '","sent",' + timestamp + ');')

  result_aux = runquery(query)

  query_id = ('SELECT max(id) from skrik.msgs;')
  result_id = runquery(query_id)
  
  result = "received " + str(result_id[0])

  return HttpResponse(result)


@csrf_exempt
def get_news(self, *args, **kwargs):
  userid_dj = kwargs.pop('userid', None)

  ##The idea here is to use fwding+a random number to check when it has been received
  random_key = str(random.randint(1,9999999))

  query_update = ('UPDATE skrik.msgs SET status="fwding-' + random_key + '" WHERE userid_to = "' + userid_dj + '";')
  result_update = runquery_multiple(query_update)

  query = ('select userid_from,message,status,timestamp,id from skrik.msgs where userid_to ="' + userid_dj + '";')

  my_query = runquery_multiple(query)
  result = json.dumps(my_query)

  return HttpResponse(result)


@csrf_exempt
def news_confirmed(self, *args, **kwargs):
  msgkey_dj = kwargs.pop('key', None)

  query_update = ('UPDATE skrik.msgs SET status="forwarded" WHERE status = "fwding-' + msgkey_dj + '";')


  result_update = runquery_multiple(query_update)

  return HttpResponse(result_update)





